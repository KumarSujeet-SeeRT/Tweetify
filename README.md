# Tweetify – AI-Powered Finance Tweet Bot

Tweetify is a fully automated AI bot that reads finance headlines (currently from Arthalogy.com), generates concise, engaging tweets using Google Gemini, posts them on Twitter via API v2, and notifies via a Telegram bot.

## 🚀 Features

- 🧠 **AI-generated finance tweets** (via Gemini-Pro / Gemini Flash)
- 📡 **Auto-fetching headlines** from any source (currently arthalogy.com)
- 🐤 **Tweets through Twitter API v2** (OAuth 2.0)
- 🔔 **Sends Telegram notification** once a tweet is posted
- ✅ **Formatted tweets** with emoji, bold heading, summary, and hashtags

## 🛠️ Tech Stack

- Python 3.10+
- Google Generative AI (Gemini)
- Twitter API v2 with OAuth 2.0
- Telegram Bot API
- dotenv (.env file for credentials)

## 🧱 Project Structure

```bash
tweetify/
│
├── main.py                  # Main runner: fetches, generates, tweets, notifies
├── headline_fetcher.py      # Scrapes headlines from arthalogy.com
├── tweet_generator.py       # Uses Gemini to generate tweet
├── .env                     # API keys and tokens
├── requirements.txt         # Required Python packages
└── README.md                # Project documentation
```

## ⚙️ Setup Instructions

### 1. 🔑 Set Up Your API Keys

Create a `.env` file in the root directory with the following:

```env
# Gemini API
GEMINI_API_KEY=your_gemini_api_key

# Twitter API v2 (OAuth 2.0 User Context)
TWITTER_CLIENT_ID=your_client_id
TWITTER_CLIENT_SECRET=your_client_secret

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### 2. 📥 Install Requirements

```bash
pip install -r requirements.txt
```

### 3. 📰 Fetching Headlines

By default, `headline_fetcher.py` scrapes headlines from:

🔗 https://arthalogy.com (inside `<div class="marquee-content">`)

You can modify this file to fetch from any other finance news source.

### 4. 🧠 Gemini for Tweet Generation

`tweet_generator.py` uses Gemini Flash or Gemini Pro to convert the headline into a clean tweet with:

- Emoji + short heading
- One-line space
- Short paragraph summary
- 1–2 relevant hashtags

✅ It avoids hallucinating fake numbers and respects the 280-character limit.

### 5. 🐤 Twitter API (OAuth 2.0)

Steps to setup:

1. Go to [Twitter Developer Portal](https://developer.twitter.com/)
2. Create a new project → App → Enable OAuth 2.0
3. Set `https://localhost:8888/callback` as your redirect URI
4. Note down:
   - Client ID
   - Client Secret

The first time you run `main.py`, it will ask you to:
- Visit the login URL
- Approve access
- Paste the redirected URL

✅ The access token will be used to tweet using `POST /2/tweets` endpoint.

### 6. 📲 Telegram Bot Notification

Steps:

1. Start a chat with [@BotFather](https://t.me/botfather)
2. Run `/newbot`, name it, and get your bot token
3. Start the bot by messaging it once
4. Visit:
   ```bash
   https://api.telegram.org/bot<YourToken>/getUpdates
   ```
5. You'll get your `chat_id` after sending a message
6. Add both in your `.env` file

## 🧪 Example Output

```
🚨 Adani Power Q1 Result

Q1 net profit dips 13.5% to ₹3,385 crore, but the board approves a 1:5 stock split! Investors will be watching how this news impacts future performance.

#AdaniPower #StockSplit
```

## 📦 Deploy/Run

```bash
python main.py
```

The bot will:
1. Scrape headline
2. Generate tweet using Gemini
3. Post on Twitter
4. Send Telegram message with timestamp

## 📋 Requirements

The following packages are required (see `requirements.txt`):

- `requests`
- `bs4`
- `tweepy`
- `python-dotenv`
- `google-generativeai`
- `requests-oauthlib`

## 📸 Screenshots

Add screenshots of your tweet, terminal logs, and Telegram message if needed.

## 📄 License

MIT License

## 👤 Author

**Sujeet Rawat** – [Arthalogy](https://arthalogy.com)

---

⭐ Star this repository if you found it helpful!
