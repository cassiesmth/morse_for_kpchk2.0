import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.chat_action import ChatActionSender
from morse_code import encode_morse_en, decode_morse_en, encode_morse_rus, decode_morse_rus 

class Form(StatesGroup):
    waiting_for_language = State()
    waiting_for_text = State()

router = Router()
user_data = {}

language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇷🇺 великая наша держава"), KeyboardButton(text="🇺🇸 god daaaamn")],
        [KeyboardButton(text="🇷🇺 морзянка, хули)"), KeyboardButton(text="🇺🇸 omg morse fr???")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@router.message(Command("start"))
async def hello_blya(message: Message):
    await message.reply(
        "сап, выбери язык, если захочешь писать на морзянке, делай пробел между символами[даж цифрами] и 3 между словами, я спать хочу и не собираюсь это обрабатывать:\nhey, choose your language plz, if you want to write in morse, put one space between characters[even numbers] and 3 spaces between words",
        reply_markup=language_keyboard
    )

@router.message(F.text.in_(["🇷🇺 великая наша держава", "🇺🇸 god daaaamn", "🇷🇺 морзянка, хули)", "🇺🇸 omg morse fr???"]))
async def language_choice(message: Message):
    if message.text == "🇷🇺 великая наша держава":
        user_data[message.from_user.id] = {"language": "ru"}
        await message.reply("оооооооооооо наш слоняра, давай сюда навальчик", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "🇺🇸 god daaaamn":
        user_data[message.from_user.id] = {"language": "en"}
        await message.reply("god dammmn bro, whatcha telling me bruh?", reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "🇷🇺 морзянка, хули)":
        user_data[message.from_user.id] = {"language": "rum"}
        await message.reply("делай пробелы между знаками пж мне лень обрабатывать, иначе не то получишь", reply_markup=types.ReplyKeyboardRemove())
    else:
        user_data[message.from_user.id] = {"language": "enm"}
        await message.reply("please insert spaces between characters im tired of handling this", reply_markup=types.ReplyKeyboardRemove())

@router.message()
async def process_user_phrase(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data or "language" not in user_data[user_id]:
        await message.reply("выбери язык сначала/fr? choose yr language:", reply_markup=language_keyboard)
        return
    
    che_visral = message.text
    user_data[user_id]["phrase"] = che_visral
    
    if user_data[user_id]["language"] == "ru":
        await message.reply(f"результат: {encode_morse_rus(che_visral)}", reply_markup=language_keyboard)
    elif user_data[user_id]["language"] == "en":
        await message.reply(f"результат: {encode_morse_en(che_visral)}", reply_markup=language_keyboard)
    elif user_data[user_id]["language"] == "rum":
        await message.reply(f"результат: {decode_morse_rus(che_visral)}", reply_markup=language_keyboard)
    elif user_data[user_id]["language"] == "enm":
        await message.reply(f"результат: {decode_morse_en(che_visral)}", reply_markup=language_keyboard)
    del user_data[user_id]

async def main():
    bot = Bot(token="apikey")
    dp = Dispatcher()
    dp.include_router(router)
    
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())