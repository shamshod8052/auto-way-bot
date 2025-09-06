from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


feedback_text = """
📲Yagona call-markaz: +998 55 514-11-15
"""

@router.message(Command("feedback"))
async def feedback_handler(message: Message):
    await message.answer(feedback_text)
