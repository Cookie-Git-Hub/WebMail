from aiogram import Router, F, Bot
from aiogram.types import Message
import app.keyboards as kb
from functions.registration import user_registration
#from functions.parsing import parsing #Доделать
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
router = Router()

bot = Bot(os.getenv('TOKEN'))

# Хэндлер на команду /start
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Привет. Я WebMail бот, к Вашим услугам! Для регистарации нажмите на кнопку 'Регистрация 📝' ", reply_markup=kb.registration)

@router.message(F.text.lower() == "регистрация 📝") #Доработать
async def registration(message: Message):
    msg = user_registration(str(message.from_user.id))
    await message.answer(msg)

# @router.message(F.text.lower() == "начать обработку 🟢") #Доработать
# async def start(message: Message):
#     await message.answer("Обработка писем началась!")
#     global stop_flag
#     while not stop_flag: 
#         parsing() #Доделать
#         await asyncio.sleep(60)
    
@router.message(F.text.lower() == "остановить обработку 🔴")
async def stop(message: Message):
    global stop_flag
    stop_flag = True
    await message.answer("Обработка писем остановлена.")

@router.message(F.text.lower() == "сменить данные ⚙️")
async def change(message: Message):
    await message.answer("Введите ваши новые данные.") #Доработать

@router.message(F.text.lower() == "авторы 👑")
async def authors(message: Message):
    await message.answer("<b>Авторы этого замечательного бота:</b>\n@CookieRevolution и @JaNoK25", parse_mode='HTML')