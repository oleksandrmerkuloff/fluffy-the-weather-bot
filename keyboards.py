from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


fluffy_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Help"),
            KeyboardButton(text="Require Geolocation", request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
