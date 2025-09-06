from aiogram import Router, F
from aiogram.types import Message

from tg_bot.keyboards import back_kb, more_back_kb

router = Router()


about_course = """
Quyidagi yo‘nalishlar bo‘yicha mutaxassislarning malakasi oshirilib, sertifikatlanadi:
1. Avtomobil yo‘llarida harakat xavfsizligini ta’minlash.
2. Avtomobil yo‘llarida buyurtmachi xizmati texnik nazorati.
3. Yo‘l xo‘jaligidagi avtotransport vositalari, maxsus texnika va mexanizmlardan foydalanish.
4. Yo‘l bo‘limlari boshliqlari uchun barcha yo‘l ishlarida ish sifatini ta’minlash
5. Avtomobil yo‘llarini qurishda loyihalashtirish, loyiha smeta hujjatlarini tayyorlash va asoslash.
6. Avtomobil yo‘llarini qurish, qayta qurish va ta’mirlash, ta’mirlashda ishlab chiqarishni tashkil etish va bajarish.
7. Ko‘priklar va sun’iy inshootlarni qurish, ta’mirlash va saqlash.
8. Avtomobil yo‘llarida geodeziya, kartografiya va kadastrni yuritish.
9. Yo‘l xo‘jaligi hamda asfaltbeton, sementbeton zavodlarida laboratoriya ishlarini tashkil etish.
10. Avtomobil yo‘llarini ta’mirlash va saqlash.
"""

more = """
Bog‘lanish uchun:
☎️Telefon raqam: +998 55-514-11-15
📱Xodim ichki raqami: 3314
"""

@router.message(F.text == "️🗃 Malaka oshirish kurslari")
async def courses_handler(message: Message):
    await message.answer(
        about_course,
        reply_markup=more_back_kb
    )

@router.message(F.text == "🕵️‍♂ Batafsil")
async def more_handler(message: Message):
    await message.answer(
        more,
        reply_markup=back_kb
    )
