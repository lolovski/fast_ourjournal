from aiogram import Router, Bot
import os

from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


import re

router = Router(name=__name__)
PHOTOS_DIR = "photos"

load_dotenv()

admin_id = os.getenv('ADMIN_ID')


@router.startup()
async def on_startup(bot: Bot):
    from bot.core.commands import set_commands
    await set_commands(bot)
    await bot.send_message(admin_id, text=f'<tg-spoiler>Начало работы</tg-spoiler>')


@router.shutdown()
async def on_shutdown(bot: Bot):
    await bot.send_message(admin_id, text=f'<tg-spoiler>КОНЕЦ!</tg-spoiler>')


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    username = re.sub(r'[^a-zA-Z0-9а-яА-ЯёЁ\s]', '', message.from_user.full_name)
    await message.answer(f"Добро пожаловать, <b>{username}</b>!")
