from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📲 Kontakt qoldirish", request_contact=True)
        ]
    ], resize_keyboard=True
)

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❓ Savol"),
            KeyboardButton(text="📄 Taklif"),
        ],
        [
            KeyboardButton(text="❕ Murojaat"),
        ]
    ], resize_keyboard=True
)

back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ], resize_keyboard=True
)

offers_list_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⚙ Texnik muammolar va ularning yechimi bo‘yicha"),
        ],
        [
            KeyboardButton(text="📃 Normativ hujjatlar va standartlarni yangilash yoki o‘zgartirishlar kiritish"),
        ],
        [
            KeyboardButton(text="🧑‍🎓 Mutaxassislarning malakasini oshirish"),
        ],
        [
            KeyboardButton(text="💈 Innovatsion materiallar va texnologiyalarni joriy etish"),
        ],
        [
            KeyboardButton(text="🧪 Ilmiy-sinov laboratoriya faoliyati bo‘yicha"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ], resize_keyboard=True
)

scientific_support_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛣 Yo‘l sohasida sizni qiynayotgan ilmiy texnik muammolar bo‘yicha yordam"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ], resize_keyboard=True
)

more_back_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕵️‍♂ Batafsil"),
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ], resize_keyboard=True
)
