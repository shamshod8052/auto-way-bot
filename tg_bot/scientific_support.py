from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.keyboards import back_kb, main_menu_kb, scientific_support_kb
from tg_bot.states import GetForm
from tg_bot.utils import send_scientific_support

router = Router()


@router.message(F.text == "❕ Murojaat")
async def support_handler(message: Message, state: FSMContext):
    await message.answer("Murojaat matnini kiriting:")
    await state.set_state(GetForm.SUPPORT)

@router.message(GetForm.SUPPORT_TYPE)
async def get_support_type_handler(message: Message, state: FSMContext):
    await state.update_data({'support_type': message.text})
    await message.answer("📝 Ilmiy yordam matnini kiriting.", reply_markup=back_kb)
    await state.set_state(GetForm.SUPPORT)

@router.message(F.content_type == ContentType.TEXT, GetForm.SUPPORT)
async def get_support_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        await send_scientific_support(message.from_user.id, support_type=data.get('support_type'), text=message.text, phone=data.get("contact"))
    except Exception as e:
        await message.answer("So'rovingiz qa'bul qilinmadi!")
    else:
        await message.answer(
            "✅ So‘rovingiz qabul qilindi. So‘rovingiz ko‘rib chiqilib, mutaxassis tomonidan xabar beriladi",
            reply_markup=main_menu_kb
        )
        await state.clear()

@router.message(GetForm.SUPPORT)
async def get_support_handler(message: Message):
    await message.reply("Iltimos faqat matnli ma'lumot kiriting!")
