"""
File: Main Telegram Fridge Bot Program
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson (credit to Niyaz Beysengulov)
Purpose: 
Timeline: Need discovered September 2023, Finished May 2024
"""
import asyncio
import imp
import logging
import sys
import os

#from time import sleep
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

from bluefors_comm import *
from backend import db_comm

load_dotenv() # will search for .env file in local folder and load variables

USER_KEY = os.getenv('MEMBER_KEY') # what users should send bot when prompted, to get access

# Initialize bot and dispatcher
# Bot token can be obtained via https://t.me/BotFather
bot = Bot(token=os.getenv('BOT_TOKEN'))
#BOT_USERNAME: '@blueforsfridgebot'
dp = Dispatcher()

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

@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command and
    """
    await message.answer("If you are a member of MSU LHQS try typing /start")


# Custom Commands
@dp.message(Command("signup"))
async def command_signup_handler(message: Message) -> None:
    """ /signup - how a new user proves they should be on the research team list"""
    # ask user to send the LHQS Bot access code.
    await message.answer("Let's get you signed up! Please respond with \"/code <the LHQS code>\" to qualify.")

@dp.message(Command("code"))
async def command_code_handler(message: Message) -> None:
    """ /code - when a new user proves they should be on the research team list"""
    given_code = str(message.text)[6:]
    await message.answer(f"I see you sent code: {given_code}")
    if given_code == USER_KEY:
        #add user id to user_list
        await message.reply("YOU DID IT!")
    else:
    #   ctr++
        await message.reply("Sorry, you've got it wrong pal.")

@dp.message(Command("checkstatus"))
async def command_status_handler(message: Message) -> None:
    """/checkstatus - to get an immediate update on the main fridge stats"""
    # get experiment chamber temp
    await message.answer("How's our fridge doin you ask?")

@dp.message(Command("errorhistory"))
async def command_errors_handler(message: Message) -> None:
    """/errorhistory - to get list of past fridge issues and dates"""
    await message.answer("Below is the error history for FRIDGEX")
# sign up for live alerts
#   add user id to alert_list


# Initiate/send warning alerts -- not sure how to do this yet
#   frequently read .txt files on comp
#   if *all these conditions*
#       send correlating error message to alert_list

async def main() -> None:
    """HOLDER...# Initialize Bot instance with a default parse mode
            which will be passed to all API calls
    #bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching"""

    await dp.start_polling(bot) #keep this at the end always


if __name__ == "__main__":
    #start_cont_check_logs() <-- bluefors_comm.py funct
    #NOTE: do I need to stop it?? or does CTR^C work? 5/13
    db_comm.create_tables()
    #TEST db_comm.add_member() <-- passed :) 5/14/24

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
