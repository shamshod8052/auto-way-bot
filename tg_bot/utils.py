import asyncio

from aiogram.exceptions import TelegramRetryAfter
from aiogram.types import Message

from config import ADMINS
from tg_bot.keyboards import contact_kb, main_menu_kb
from loader import bot


async def give_contact(message: Message):
    await message.answer(
        "<b>❗️ Iltimos, bizga murojaat qilish uchun “Kontakt qoldirish” tugmasi orqali ulaning.</b>",
        reply_markup=contact_kb
    )

async def set_main_menu(message: Message):
    await message.answer(
        "<b>❗ Eslatib o‘tamiz, murojaatingiz faqatgina yo‘l sohasida yangi innovatsion g‘oyalar, "
        "takliflar yoki ushbu sohada sizni qiynayotgan texnik muammolar (<i>Izoh: shikoyat va arizalar ko‘rib "
        "chiqilmaydi</i>) hamda yo‘l xo‘jaligi sohasida mutaxassislarning malakasini oshirish bilan bog‘liq "
        "bo‘lishiga e’tibor qarating!</b>",
        reply_markup=main_menu_kb
    )

async def send_msg(chat_id, text, n=1):
    if n > 3:
        return
    try:
        await bot.send_message(chat_id, text)
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after)
        await send_msg(chat_id, text, n + 1)
    except:
        await send_msg(chat_id, text, n + 1)

async def send_question(user_id, text, phone=''):
    for admin in ADMINS:
        await send_msg(
            admin,
            f"❕ <b>User ID:</b> <code>{user_id}</code>\n"
            f"📞 <b>Telefon:</b> {phone}\n\n"
            f"<b>Savol:</b>\n{text}"
        )

async def send_offer(user_id, offer_type, text, phone=''):
    for admin in ADMINS:
        await send_msg(
            admin,
            f"❕ <b>User ID:</b> <code>{user_id}</code>\n"
            f"📞 <b>Telefon:</b> {phone}\n\n"
            f"<b>Taklif turi:</b>\n"
            f"{offer_type}\n\n"
            f"<b>Taklif:</b>\n"
            f"{text}"
        )

async def send_scientific_support(user_id, support_type, text, phone=''):
    for admin in ADMINS:
        await send_msg(
            admin,
            f"❕ <b>User ID:</b> <code>{user_id}</code>\n"
            f"📞 <b>Telefon:</b> {phone}\n\n"
            f"<b>Yordam turi:</b>\n"
            f"{support_type}\n\n"
            f"<b>Ilmiy yordam</b>\n"
            f"{text}"
        )

async def send_answer(user_id, answer):
    await send_msg(user_id, answer)
