# from Bot.tools.keyboards import *
from aiogram import types, Router
from aiogram.filters import CommandStart, Command
# from Bot.tools import database, utils, fsm
from aiogram.fsm.context import FSMContext


for_all_users = Router()


@for_all_users.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Добро пожаловать в Юрист-бот, чем я могу быть вам полезен?")
