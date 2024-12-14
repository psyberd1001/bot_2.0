from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from venv1.bot.keyboard.Reply.menu_kb_reply import menu_kb

router = Router()


@router.message(Command('start'))
async def command_start(message: Message):
    await message.answer(f'Привет {message.from_user.full_name}!'
                         '\nЯ бот помогающий твоему <здоровью>!'
                         '\nВведи команду Calories, чтобы узнать свою норму калориев', reply_markup=menu_kb())

