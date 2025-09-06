from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.utils import give_contact

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await give_contact(message)
