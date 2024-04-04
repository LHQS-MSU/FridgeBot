# Telgram bot for fridge stability tracking using aiogram
# INSTALL...
# pip install python-telegram-bot ??may not be needed
# pip install -U aiogram

from time import sleep

from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='6789765586:AAE-XUmzOAfF_X6fVrNiFCn7Wln4yD5jWcs')
#BOT_USERNAME: '@blueforsfridgebot'
dp = Dispatcher(bot)

# Start - what happens when the user finds the bot and clicks "start"
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Welcome! To continue, please send the LHQS Bot access code.")
#   if proper code, add user id to user_list
#   else if user id in denied_list
#       "Sorry, looks like we're done here."
#   else
#       ctr++
#       "Sorry, you've got it wrong pal!"
    pass

# Custom Commands
@dp.message_handler()
async def tempcheck(message: types.Message):
# get experiment chamber temp
    await message.answer(message.text)

# get fridge error history
 
# sign up for live alerts
#   add user id to alert_list


# Initiate/send warning alerts -- not sure how to do this yet
#   frequently read .txt files on comp
#   if *all these conditions*
#       send correlating error message to alert_list

executor.start_polling(dp) #keep this at the end of the file!