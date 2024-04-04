import os
import logging
from newinstruments.BlueFors import BlueFors
from time import sleep

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import bold, hspoiler, text

bf = BlueFors()

def get_user_info(index: int) -> dict:
    name = os.getenv(f"USER{index}_NAME")
    idx = int(os.getenv(f"USER{index}_ID"))
    return {"name": name, "idx": idx}

API_TOKEN = os.getenv('API_TOKEN')
admin = get_user_info(1)
user2 = get_user_info(2)
user3 = get_user_info(3)
user4 = get_user_info(4)
user5 = get_user_info(5)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
id_name = [admin["name"], user2["name"], user3["name"], user4["name"], user5["name"]]
id_list = [admin["idx"], user2["idx"], user3["idx"], user4["idx"], user5["idx"]]

id_name0 = [admin["name"]]
id_list0 = [admin["idx"]]

trusted_ids = [admin["idx"], user2["idx"], user3["idx"], user4["idx"]]

def auth(func):

    async def wrapper(message):
        if message['from']['id'] not in id_list:
            return await message.reply("You shall not pass!", reply=False)
        return await func(message)
    
    return wrapper


@dp.message_handler(commands=['start', 'help'])
@auth
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    id_index = id_list.index(message['from']['id'])
    await message.reply(f"Hi {id_name[id_index]}!\nI'm telexp bot!\nPowered by aiogram, dev Niyaz.\n"
    "This bot provides the status of \nBlueFors Helios \n"
    "Type /status to get fridge status",
    reply=False)

@dp.message_handler(commands=['status'])
@auth
async def get_status(message: types.Message):
    bluefors_status = bf.get_status_all()
    global johannes_counter
    if message['from']['id'] == user5["idx"]:
        if johannes_counter > 0: 
            full_message = f'<tg-spoiler> REMAINING ATTEMPTS: {johannes_counter}</tg-spoiler> \n \n' +  bluefors_status
            johannes_counter = johannes_counter - 1
            await message.reply(full_message, reply=False, parse_mode= 'HTML')
        else:
            final_message = 'WARNING \nMaster protocol has been initiated \nOpening V18 and V19 to vent \nPlease wait...'
            joephoto = open('thumbnail_subject.jpg', 'rb')
            await message.reply(final_message, reply=False)
            sleep(5)
            await bot.send_photo(user5["idx"], joephoto)
            for id in trusted_ids:
                joephoto = open('thumbnail_subject.jpg', 'rb')
                await bot.send_photo(id, joephoto)
    else:
        await message.reply(bluefors_status, reply=False, parse_mode= 'HTML')

@dp.message_handler(commands=['christmas'])
@auth
async def christmas_message(message: types.Message):
    bluefors_status = bf.get_status_all()
    if message['from']['id'] == admin["idx"]:
        for id, name in zip(id_list, id_name):
            with open('MerryChristmas.jpg', 'rb') as photo:
                await bot.send_photo(id, photo, caption=f'{name}, Merry Christmas🎄🎄🎄', parse_mode='HTML')
                sleep(10)
                await bot.send_message(id, '<tg-spoiler> and here is the latest HELIOS system status: \n \n '+bluefors_status+'</tg-spoiler>', parse_mode= 'HTML')

if __name__ == '__main__':
    johannes_counter = 200_000
    executor.start_polling(dp, skip_updates=True)