from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.utils import set_main_menu

router = Router()

@router.message(F.content_type == ContentType.CONTACT)
async def contact_handler(message: Message, state: FSMContext):
    await state.update_data({'contact': message.contact.phone_number})
    await set_main_menu(message)
