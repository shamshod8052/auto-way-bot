from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.utils import set_main_menu

router = Router()


@router.message(F.text == "⬅️ Orqaga")
async def main_menu_handler(message: Message, state: FSMContext):
    await state.set_state(state=None)
    await set_main_menu(message)
