import asyncio
import datetime
import logging
import sys

from aiogram import Bot

from config import ADMINS
from loader import dp, bot
from tg_bot import router
from tg_bot.middleware import ContactCheckMiddleware


async def on_startup_notify(bot: Bot):
    bot_ = await bot.me()
    print(f"############ Bot ishga tushdi | ID: {bot_.id} | USERNAME: @{bot_.username} ############")
    print(f"Started time: {datetime.datetime.now()}")

    for admin in ADMINS:
        try:
            await bot.send_message(admin, "Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)


async def main():
    await on_startup_notify(bot)
    dp.message.middleware(ContactCheckMiddleware())
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR, stream=sys.stdout)
    asyncio.run(main())
