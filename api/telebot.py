import logging
from datetime import datetime

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from api.main import ROOT_URL

API_TOKEN = '6260643124:AAHzDUFw8tNc34K4Ws48uAr6onnrmG2-2sY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    # Create the inline keyboard
    keyboard = InlineKeyboardMarkup()
    # Create the buttons
    button1 = InlineKeyboardButton(text='Namoz vaqtlari', callback_data='button1')
    # Add the buttons to the keyboard
    keyboard.add(button1)
    # Send the message with the inline keyboard
    await message.reply("Namoz vaqtlarini ko'rish uchun quyidagi tugmani boshing!", reply_markup=keyboard)


# # Define a handler for the /start command
# @dp.message_handler(commands=['btn'])
# async def button_type(message: types.Message):


@dp.callback_query_handler(lambda query: query.data == 'button1')
async def button1_callback(query: types.CallbackQuery):
    day = datetime.now().day
    date = ROOT_URL.json()['data'][day - 1]['date']['readable']
    weekday = ROOT_URL.json()['data'][day - 1]['date']['gregorian']['weekday']['en']
    fajr = ROOT_URL.json()['data'][day - 1]['timings']['Fajr']
    sunrise = ROOT_URL.json()['data'][day - 1]['timings']['Sunrise']
    dhuhr = ROOT_URL.json()['data'][day - 1]['timings']['Dhuhr']
    asr = ROOT_URL.json()['data'][day - 1]['timings']['Asr']
    maghrib = ROOT_URL.json()['data'][day - 1]['timings']['Maghrib']
    hufton = ROOT_URL.json()['data'][day - 1]['timings']['Isha']

    text_message = f"\n📆 {date} \n\n Hafta kuni: {weekday}  \n \n🏙 Tong: {fajr} 🕒 \n\n🌅 Bomdod: {sunrise} 🕓 \n\n🏞 Peshin: {dhuhr} 🕛 \n\n🌇 Asr: {asr} 🕟 \n\n🌆 Shom: {maghrib} 🕢 \n\n🌃 Hufton: {hufton} 🕘\n"
    await query.answer("Sending...")
    await bot.send_message(chat_id=query.message.chat.id, text=text_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
