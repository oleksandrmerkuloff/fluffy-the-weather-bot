import aiogram
import asyncio
from aiogram.types import FSInputFile

import os

from keyboards import fluffy_kb
from API import weather_api as wapi


BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = aiogram.Bot(BOT_TOKEN)
dp = aiogram.Dispatcher()


@dp.message(aiogram.F.text.endswith("start"))
async def start_command(message: aiogram.types.Message) -> None:
    with open("fluffy_text\\greeting.txt", "r", encoding="utf-8") as file:
        greeting = file.readlines()[0]
    await bot.send_message(message.chat.id, greeting, reply_markup=fluffy_kb)


@dp.message(aiogram.F.text.title() == "Help")
async def help_command(message: aiogram.types.Message) -> None:
    with open("fluffy_text\\help.txt", "r", encoding="utf-8") as file:
        greeting = file.readlines()[0]
    await bot.send_message(message.chat.id, greeting, reply_markup=fluffy_kb)


@dp.message()
async def get_location(message: aiogram.types.Message): 
    try:
        if message.location:
            coordinates = (
                message.location.latitude,
                message.location.longitude,
            )
            image_name, weather = wapi.get_current_weather_data(coordinates)
        else:
            image_name, weather = wapi.geocoding(message.text)
        photo = FSInputFile(f"images/{image_name}.jpg")
        await bot.send_photo(message.chat.id, photo)
        await bot.send_message(message.chat.id, weather)
    except IndexError:
        await message.answer("Вибачте, такого міста не існує. Повторіть спробу.")


async def main():
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
