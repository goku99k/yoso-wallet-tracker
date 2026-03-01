import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("BOT_TOKEN:", TOKEN)
print("CHAT_ID:", CHAT_ID)

bot = Bot(token=TOKEN)

bot.send_message(
    chat_id=CHAT_ID,
    text="✅ Test message from GitHub Actions"
)

print("Message sent successfully")
