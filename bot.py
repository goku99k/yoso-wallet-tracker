import requests
import time
import os
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

previous_data = {}
buy_message_ids = {}

def get_top_wallets():
    url = "https://yoso.fun/leaderboard"
    response = requests.get(url)
    return response.text

def parse_wallets(html):
    # VERY SIMPLE placeholder parsing (we will improve later)
    wallets = {}
    lines = html.split("\n")

    for line in lines:
        if "0x" in line:
            wallet = line.strip()
            wallets[wallet] = "ACTIVE"

    return dict(list(wallets.items())[:5])

while True:
    try:
        data = parse_wallets(get_top_wallets())

        for wallet in data:
            if wallet not in previous_data:
                msg = bot.send_message(
                    chat_id=CHAT_ID,
                    text=f"🟢 BUY detected\nWallet: {wallet}"
                )
                buy_message_ids[wallet] = msg.message_id

        for wallet in previous_data:
            if wallet not in data:
                if wallet in buy_message_ids:
                    bot.send_message(
                        chat_id=CHAT_ID,
                        text=f"🔴 SELL detected\nWallet: {wallet}",
                        reply_to_message_id=buy_message_ids[wallet]
                    )

        previous_data = data
        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(60)
