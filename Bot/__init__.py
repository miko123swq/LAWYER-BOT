import asyncio
import os
from config import *
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import CommandStart



bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router

def register_handlers():
    from .handlers import commands
    commands.register_handlers(dp)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Юрист-бот начал свою работу")
    await dp.start_polling(bot)

