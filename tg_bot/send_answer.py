from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import ADMINS
from tg_bot.states import GetForm
from tg_bot.filters import AdminFilter
from tg_bot.utils import send_answer
from tg_bot.keyboards import main_menu_kb

router = Router()

@router.message(AdminFilter(ADMINS), Command("answer"))
async def answer_handler(message: Message, state: FSMContext):
    await message.answer("Javob yubormoqchi bo'lgan mijoz \"USER ID\"sini yuboring.\n\nMasalan: 123456789")
    await state.set_state(GetForm.GET_USER_ID)

@router.message(GetForm.GET_USER_ID)
async def get_user_id_handler(message: Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Xato ma'lumot kiritildi!")
    await state.update_data({'user_id': int(message.text)})
    await message.answer("<b>Javob matnini kiriting.</b>")
    await state.set_state(GetForm.ANSWER)

@router.message(GetForm.ANSWER, F.content_type == ContentType.TEXT)
async def get_answer_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = int(data.get('user_id'))
    answer = message.text
    try:
        await send_answer(user_id, answer)
    except Exception as e:
        await message.answer("Javob yuborilmadi!")
    else:
        await message.answer("✅ Javob yuborildi!", reply_markup=main_menu_kb)
        await state.clear()

@router.message(GetForm.ANSWER)
async def get_answer_handler(message: Message):
    await message.reply("Iltimos faqat matnli ma'lumot kiriting!")
