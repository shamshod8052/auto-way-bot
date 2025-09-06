from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.keyboards import back_kb, main_menu_kb
from tg_bot.states import GetForm
from tg_bot.utils import send_question

router = Router()


@router.message(F.text == "❓ Savol")
async def quest_handler(message: Message, state: FSMContext):
    await message.answer("📝 Savolni kiriting", reply_markup=back_kb)
    await state.set_state(GetForm.QUESTION)

@router.message(F.content_type == ContentType.TEXT, GetForm.QUESTION)
async def get_question_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        await send_question(message.from_user.id, text=message.text, phone=data.get("contact"))
    except Exception as e:
        await message.answer("Savolingiz yuborilmadi!")
    else:
        await message.answer("✅ Savolingiz ko‘rib chiqish uchun qabul qilindi.", reply_markup=main_menu_kb)
        await state.clear()

@router.message(GetForm.QUESTION)
async def get_question_handler(message: Message):
    await message.reply("Iltimos faqat matnli ma'lumot kiriting!")
