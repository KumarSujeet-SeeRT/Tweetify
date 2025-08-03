import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def generate_tweet(headline: str) -> str:
    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = (
        f"You are a financial content writer. Write a Twitter post under 280 characters for the following headline:\n\n"
        f"'{headline}'\n\n"
        "Tweet format:\n"
        "1. Start with a relevant emoji (e.g., 🚨, 📢) followed by a short, flexible 2–4 word title summarizing the news.\n"
        "2. Add a blank line.\n"
        "3. Write a short, natural-sounding summary of the news, using only the info from the headline. No made-up data.\n"
        "4. End with 1–2 relevant hashtags.\n"
        "Keep the tone crisp, clear, and professional. Do not exceed 280 characters total."
    )



    response = model.generate_content(prompt)
    return response.text.strip()
