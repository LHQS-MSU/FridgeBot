import asyncio
import os
import sys
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import logging

load_dotenv()
# Your bot token
API_TOKEN = os.getenv('BOT_TOKEN') # Bot token can be obtained via https://t.me/BotFather

# List of user IDs to send the message to
users = [6783498213]

# Initialize the bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def send_first_message():
    message = "Hello! This is the first message from the bot."

    for user_id in users:
        try:
            await bot.send_message(user_id, message)
            print(f"Message sent to user {user_id}")
        except Exception as e:
            print(f"Failed to send message to user {user_id}: {e}")

async def main():
    # Start the bot
    await dp.start_polling(bot)

    # Send the first message to users
    await send_first_message()

    # Stop the bot
    await dp.stop_polling(bot)
    await bot.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
