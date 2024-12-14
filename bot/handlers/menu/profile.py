from aiogram import Router, F, Bot, Dispatcher
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from venv1.bot.config import bot_token
import re
import asyncio



def extract_number(text):
    match = re.search(r'\b(\d+)\b', text)
    if match:
        return int(match.group(1))
    else:
        return None

class Form(StatesGroup):
    name = State()
    age = State()
    long_1 = State()
    mass = State()


router = Router()

bot = Bot(bot_token)
dp = Dispatcher(storage=MemoryStorage())


@router.message(F.text == 'Calories')
async def start_process(message: Message, state: FSMContext):
    await asyncio.sleep(2)
    await message.answer('Привет. Напиши как тебя зовут: ')
    await state.set_state(Form.name)

@router.message(F.text, Form.name)
async def capture_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await asyncio.sleep(2)
    await message.answer('А теперь сколько тебе полных лет: ')
    await state.set_state(Form.age)

@router.message(F.text, Form.age)
async def capture_long(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await asyncio.sleep(2)
    await message.answer('Пол пути пройдено! Теперь меня интересует твой рост: ')
    await state.set_state(Form.long_1)

@router.message(F.text, Form.long_1)
async def capture_mass(message: Message, state: FSMContext):
    await state.update_data(long_1=message.text)
    await asyncio.sleep(2)
    await message.answer('Финишная прямая! Последний вопрос, каков твой вес? В киллограммах: ')
    await state.set_state(Form.mass)

@router.message(F.text, Form.mass)
async def capture_age1(message: Message, state: FSMContext):
    await state.update_data(mass=message.text)
    await asyncio.sleep(2)

    data = await state.get_data()
    result1 = extract_number(data.get("age"))
    result2 = extract_number(data.get("long_1"))
    result3 = extract_number(data.get("mass"))
    result4 = (result3 * 10 + 6.25 * float(result2)) - (5 * result1) + 5
    msg_text = (f'Вас зовут {data.get("name")} и вам {data.get("age")} лет, а так же ваш рос равен: {data.get("long_1")}, а ваш вес: ' 
                f'{data.get("mass")} '
                f'\nСпасибо за то что ответили на мои вопросы.\n Ваша норма углеводов: {result4}')
    await message.answer(msg_text)
    await state.clear()

