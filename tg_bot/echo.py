from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.keyboards import main_menu_kb

router = Router()

@router.message()
async def echo_handler(message: Message, state: FSMContext):
    await state.set_state(state=None)
    await message.answer("Iltimos menyudan kerakli bo'limni tanlang!", reply_markup=main_menu_kb)
