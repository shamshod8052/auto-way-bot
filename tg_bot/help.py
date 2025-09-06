from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


help_text = """
Buyruqlar: 
/start - Botni ishga tushirish
/help - Yordam
/feedback - Biz bilan bog'lanish
"""

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(help_text)
