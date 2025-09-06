from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.keyboards import back_kb, main_menu_kb, offers_list_kb
from tg_bot.states import GetForm
from tg_bot.utils import send_offer

router = Router()


@router.message(F.text == "📄 Taklif")
async def offer_handler(message: Message, state: FSMContext):
    await message.answer("Taklif turini tanlang.", reply_markup=offers_list_kb)
    await state.set_state(GetForm.OFFER_TYPE)

@router.message(GetForm.OFFER_TYPE)
async def get_offer_type_handler(message: Message, state: FSMContext):
    await state.update_data({'offer_type': message.text})
    await message.answer("📝 Taklifni kiriting.", reply_markup=back_kb)
    await state.set_state(GetForm.OFFER)

@router.message(F.content_type == ContentType.TEXT, GetForm.OFFER)
async def get_offer_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    try:
        await send_offer(message.from_user.id, offer_type=data.get('offer_type'), text=message.text, phone=data.get("contact"))
    except Exception as e:
        await message.answer("Taklif yuborilmadi!")
    else:
        await message.answer(
            "✅ Taklifingiz uchun rahmat. Taklifingiz o‘rganib chiqilib, natijasi sizga ma’lum qilinadi.",
            reply_markup=main_menu_kb
        )
        await state.clear()

@router.message(GetForm.OFFER)
async def get_offer_handler(message: Message):
    await message.reply("Iltimos faqat matnli ma'lumot kiriting!")
