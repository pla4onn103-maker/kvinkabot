import asyncio
import json
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="9246776761:AAE-WzA66mvyeY9WwFmUM-yBeheB4yuJVT4")
dp = Dispatcher()
    
@dp.message()
async def cmd_message(message: types.Message):
    print(f"{message.from_user.username} - {message.text}")
    text = message.text
    if message.photo:
        await message.answer("ахвахаххаха папалса пыдарасэна ыхыхыхыхыхых")
        return

    if "привет" in text:
        await message.answer("привет! Я квинка, настоящая! Что ты хочешь? Робуксы звезды или подарки? напиши мне об этом!")

    if "скам" in text:
        await message.answer("Нет, ты чего, я не скам!")


    if "звезд" in text or "звёзд" in text or "подар" in text or "робукс" in text or "робакс" in text:
        await message.answer("Сначала сфоткай маминку карточку с двух сторон и перепиши на меня квартиру! Не бойся, я точно не 40 летний Андрей Чикатило который хочет спиздить все твои деньги.")


async def main():
    print("Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
