"""
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson (credit to Niyaz Beysengulov)
Purpose: 
Timeline: Need discovered September 2023, Finished May 2024
"""
import asyncio
#from distutils.cmd import Command # pip install -U aiogram
import logging
import sys
import os

from aiogram import Bot, Dispatcher #Router, types #executor
#from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
#from aiogram.filters.command import CommandObject
from aiogram.types import Message
from telegram.ext import ConversationHandler
from dotenv import load_dotenv

load_dotenv() # will search for .env file in local folder and load variables

API_TOKEN = os.getenv('BOT_TOKEN') # Bot token can be obtained via https://t.me/BotFather
USER_KEY = os.getenv('MEMBER_KEY') # what users should send bot when prompted, to get access

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher() # All handlers should be attached to the Router (or Dispatcher)

validated_users = [] #list, nameID
previous_user_history = {} #dict, nameID:attempts
denied_users = [] #so we don't waste our time
ATTEMPT1, ATTEMPT2, ATTEMPT3, FINALRESULT = range(4)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command and
    What happens when the user finds the bot and clicks "start"
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    #GIVEN: await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer(F"Welcome {message.from_user.full_name}! Now please /signup")
    print(F"ID {message.from_user.id}")
    print(F"NAME {message.from_user.first_name}")


# Custom Commands...

@dp.message(Command("signup"))
async def command_signup_handler(message: Message) -> None:
    """ /signup - how a new user proves they should be on the research team list"""
    # ask user to send the LHQS Bot access code.
    await message.answer("Let's get you signed up! Please respond with the LHQS code to qualify.")
    # if proper code, add user id to user_list
    #await message.reply("")
    # else if user id in denied_list
    #   "Sorry, looks like we're done here."
    # else
    #   ctr++
    #   "Sorry, you've got it wrong pal!"

'''@dp.message(ConversationHandler( #Still working on it!... 12/15
    entry_points=[Command("signup")],
    states={
        ATTEMPT1: [],
        ATTEMPT2: [],
        ATTEMPT3: [],
        FINALRESULT: []
    },
    fallbacks=[CommandStart()],
))'''

@dp.message(Command("checkstatus"))
async def command_status_handler(message: Message) -> None:
    """/checkstatus - to get an immediate update on the main fridge stats"""
    await message.answer("How's our fridge doin you ask?")

@dp.message(Command("errorhistory"))
async def command_errors_handler(message: Message) -> None:
    """/errorhistory - to get list of past fridge issues and dates"""
    await message.answer("Below is the error history for FRIDGEX")

#@dp.message()
#async def echo_handler(message: types.Message) -> None:
    #EXAMPLE - Handler will forward receive a message back to the sender

    #By default, message handler will handle all message types (like a text, photo, sticker etc.)
#    try:
        # Send a copy of the received message
#        await message.send_copy(chat_id=message.chat.id)
#    except TypeError:
        # But not all the types is supported to be copied so need to handle it
#        await message.answer("Nice try!")

async def main() -> None:
    """HOLDER...# Initialize Bot instance with a default parse mode
            which will be passed to all API calls
    #bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching"""
    await dp.start_polling(bot) #keep this at the end always


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
