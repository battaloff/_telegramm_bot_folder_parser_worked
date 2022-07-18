from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot)


if __name__ == "__main__":
    from handler import *
    executor.start_polling(dp, skip_updates=True)
