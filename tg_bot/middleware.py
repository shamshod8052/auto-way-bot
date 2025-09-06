from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.enums import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tg_bot.utils import give_contact


# Middleware
class ContactCheckMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        state: FSMContext = data["state"]

        # Har doim contact borligini tekshirish
        stored_data = await state.get_data()
        if "contact" not in stored_data and event.text not in ["/start"] and event.content_type != ContentType.CONTACT:
            await give_contact(event)
            return  # handler ishlamaydi

        return await handler(event, data)
