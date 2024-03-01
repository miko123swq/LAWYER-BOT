from aiogram import Router, Dispatcher, F
from aiogram.filters import Command, CommandStart
from main import *

def register_handlers(dp: Dispatcher):
    dp.message.register(start_cmd, CommandStart())




