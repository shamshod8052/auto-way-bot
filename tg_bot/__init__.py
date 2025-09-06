from aiogram import Router

from tg_bot.start import router as router1
from tg_bot.get_contact import router as router2
from tg_bot.help import router as router3
from tg_bot.main_menu import router as router4
from tg_bot.quest import router as router5
from tg_bot.offer import router as router6
from tg_bot.scientific_support import router as router7
from tg_bot.feedback import router as router8
from tg_bot.send_answer import router as router9
from tg_bot.courses import router as router10
from tg_bot.echo import router as router11


router = Router()

router.include_router(router1)
router.include_router(router2)
router.include_router(router3)
router.include_router(router4)
router.include_router(router5)
router.include_router(router6)
router.include_router(router7)
router.include_router(router8)
router.include_router(router9)
router.include_router(router10)
router.include_router(router11)
