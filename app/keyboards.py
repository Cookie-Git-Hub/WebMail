from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

main_kb = [
    [KeyboardButton(text="Начать обработку 🟢"),
    KeyboardButton(text="Остановить обработку 🔴")],
    [KeyboardButton(text="Сменить данные ⚙️"),
    KeyboardButton(text="Авторы 👑")]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')

registration_kb = [
    [KeyboardButton(text="Регистрация 📝")]
]

registration = ReplyKeyboardMarkup(keyboard=registration_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')