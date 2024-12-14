from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(F.text == 'Формула')
async def command_start(message: Message):
    kb_project_url = InlineKeyboardBuilder()
    kb_project_url.row(types.InlineKeyboardButton(
        text="Наш канал", url="https://pwonline.ru/")
    )
    await message.reply(f' Упрощенный вариант формулы Миффлина-Сан Жеора: '
                        f'\nдля мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;', reply_markup=kb_project_url.as_markup())

# @router.message()
# async def echo_handler(message: Message):
#     try:
#         await message.answer('Введите команду, а не случайный текст!')
#     except TypeError:
        # await message.answer("Nice Try!")