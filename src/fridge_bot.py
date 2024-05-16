"""
File: Main Telegram Fridge Bot Program
Project: Telegram Bot LHQS Fridge Alert System
Developer: Abby Peterson (credit to Niyaz Beysengulov)
Purpose: 
Timeline: Need discovered September 2023, Finished May 2024
"""
import asyncio
import logging
import sys
import os

#from time import sleep
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

from bluefors_comm import * #tbd which methods exactly
from backend import db_comm

load_dotenv() # will search for .env file in local folder and load variables

USER_KEY = os.getenv('MEMBER_KEY') # what users should send bot when prompted, to get access

# Initialize bot and dispatcher
# Bot token can be obtained via https://t.me/BotFather
bot = Bot(token=os.getenv('BOT_TOKEN'))
#BOT_USERNAME: '@blueforsfridgebot'
dp = Dispatcher()

def auth(func):
    '''FILLER'''
    async def wrapper(message):
        '''FILLER'''
        if not db_comm.is_member(message.from_user.id):
            return await message.reply("You shall not pass! Try /signup first.", reply=False)
        return await func(message)
    return wrapper

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
    await message.answer(F"Welcome {message.from_user.full_name}! Now please /signup")
    print(F"ID {message.from_user.id}")
    print(F"NAME {message.from_user.first_name}")

# Custom Commands
@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    This handler receives messages with `/help` command and
    """
    #TODO: make much more detailed & helpful lol
    #GIVEN: await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer("If you are a member of MSU LHQS try typing /start")

@dp.message(Command("signup"))
async def command_signup_handler(message: Message) -> None:
    """ /signup - how a new user proves they should be on the research team list"""
    # ask user to send the LHQS Bot access code.
    await message.answer("Please respond with \"/code <the LHQS code>\" to get signed up.")

@dp.message(Command("code"))
async def command_code_handler(message: Message) -> None:
    """ /code - when a new user proves they should be on the research team list"""
    given_code = str(message.text)[6:]
    await message.answer(f"I see you sent code: {given_code}")
    if given_code == USER_KEY:
        db_comm.add_member((message.from_user.id),(message.from_user.full_name))
        await message.reply("You now have access to our fridge information now!\n\
            I also assumed you wanted to be signed up for alerts. If that was\
                presumptuous of me, just respond with /stopalerts")
    else:
        await message.reply("Sorry, you've got it wrong pal.")

@dp.message(Command("checkstatus"))
@auth
async def command_status_handler(message: Message) -> None:
    """/checkstatus - to get an immediate update on the main fridge stats"""
    # TODO: get experiment chamber temp using bluefors_comm.py
    await message.answer("How's our fridge doin you ask?")

@dp.message(Command("errorhistory"))
@auth
async def command_errors_handler(message: Message) -> None:
    """/errorhistory - to get list of past fridge issues and dates"""
    # TODO: pull from db_comm.py for the fridge table's data
    await message.answer("Below is the error history for FRIDGEX")

@dp.message(Command("getalerts"))
@auth
async def command_yesalert_handler(message: Message) -> None:
    """FILLER"""
    # 1: on, get alerts - 0: off, no more alerts
    db_comm.alert_choice((message.from_user.id),1)
    await message.answer("Alrighty, you're signed up for alerts!")

@dp.message(Command("stopalerts"))
@auth
async def command_noalert_handler(message: Message) -> None:
    """FILLER"""
    # 1: on, get alerts - 0: off, no more alerts
    db_comm.alert_choice((message.from_user.id),0)
    await message.answer("Okay okay, we stopped your alerts. Miss you!")

# TODO: Initiate/send warning alerts -- not sure how to do this yet
#   frequently read .txt files on comp
#   if *all these conditions*
#       send correlating error message to alert_list
async def send_alert_message(message):
    users = db_comm.get_alert_list() #["6783498213"]

    for user_id in users:
        try:
            await bot.send_message(user_id, message)
            print(f"Message sent to user {user_id}")
        except Exception as e:
            print(f"Failed to send message to user {user_id}: {e}")

async def main() -> None:
    """FILLER"""
    # Send the first message to users
    await send_alert_message("FALSE ALARM")
    
    await dp.start_polling(bot) #keep this at the end always


if __name__ == "__main__":
    #TODO: start_cont_check_logs() <-- bluefors_comm.py funct
    #NOTE: do I need to stop it?? or does CTR^C work? 5/13

    db_comm.create_tables()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
