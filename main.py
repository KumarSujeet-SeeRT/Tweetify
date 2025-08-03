import os
import requests
from dotenv import load_dotenv
from tweet_generator import generate_tweet
from headline_fetcher import fetch_headlines
from datetime import datetime
from requests_oauthlib import OAuth2Session

load_dotenv()

# --- Twitter OAuth 2.0 Configuration ---
CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
REDIRECT_URI = "https://localhost:8888/callback"  # Must match Twitter developer portal

AUTH_BASE_URL = "https://twitter.com/i/oauth2/authorize"
TOKEN_URL = "https://api.twitter.com/2/oauth2/token"
SCOPES = ["tweet.write", "users.read", "offline.access"]

# Create OAuth2 session
twitter = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPES)
auth_url, state = twitter.authorization_url(AUTH_BASE_URL, code_challenge_method="S256")

print("Open this link in your browser and authorize the app:")
print(auth_url)

redirect_response = input("\n Paste the full redirect URL here: ").strip()

# Exchange code for access token
token = twitter.fetch_token(
    TOKEN_URL,
    authorization_response=redirect_response,
    client_secret=CLIENT_SECRET,
    include_client_id=True,
    code_verifier=twitter._client.code_verifier
)

# --- Tweet Preparation ---
headline = fetch_headlines()  
raw_tweet = generate_tweet(headline)

def bold_heading(tweet):
    if "\n\n" in tweet:
        lines = tweet.split("\n\n")
        heading = f"**{lines[0].strip()}**"
        return f"{heading}\n\n{lines[1].strip()}"
    return tweet

tweet = bold_heading(raw_tweet)

# --- Post to Twitter ---
def post_to_twitter(tweet_text):
    try:
        response = twitter.post(
            "https://api.twitter.com/2/tweets",
            json={"text": tweet_text}
        )
        if response.status_code == 201:
            print("✅ Tweet posted successfully.")
            return True
        else:
            print(f"❌ Failed to post tweet: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print("❌ Error posting tweet:", e)
        return False

# --- Telegram Notification ---
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        r = requests.post(url, data=payload)
        print("✅ Telegram notification sent.")
    except Exception as e:
        print("❌ Telegram send error:", e)

# --- Run ---
if __name__ == "__main__":
    if post_to_twitter(tweet):
        send_telegram_message(f"✅ Tweet posted at {datetime.now().strftime('%H:%M:%S')}:\n\n{tweet}")
    else:
        send_telegram_message("🔴 Failed to post tweet.")
