# 📄 **Avtomobil yo’llari ilmiy-tadqiqot instituti murojaat boti**

Avtomobil yo‘llari ilmiy-tadqiqot instituti tomonidan ishlab chiqilgan ushbu Telegram bot orqali foydalanuvchilar **avtomobil yo‘llari qo‘mitasi** va uning tizim korxonalarida yuz berayotgan:

* korrupsiya holatlari haqida murojaat qilish
* qonun buzilishi bilan bog‘liq xabarlar yuborish
* savol va takliflarni jo‘natish

imkoniyatiga ega bo‘ladilar.

Botning asosiy maqsadi — **shaffoflikni oshirish**, qonun buzilishlarning oldini olish va tizimni rivojlantirishga ko‘maklashishdir.

## 🔗 Telegram Bot
👉 [@uzavtoyul_anticorBot](https://t.me/uzavtoyul_anticorBot)

---

## 🚀 **Texnologiyalar**

* **Python 3.11**
* **aiogram 3.22.0** — Telegram bot framework
* **PostgreSQL** — ma’lumotlar bazasi

---

## 🔧 **O‘rnatish bo‘yicha ko‘rsatma**

### 1️⃣ Repository’ni klon qilish

```bash
git clone https://github.com/shamshod8052/auto-way-bot
cd auto-way-bot
```

### 2️⃣ Virtual environment yaratish

#### Windows uchun:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS uchun:

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Kerakli kutubxonalarni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## 🔐 **Environment variables (`.env`)**

Loyiha ishga tushishi uchun quyidagi muhit o‘zgaruvchilarini to‘ldiring:

```
BOT_TOKEN=""
ADMINS=1
```

`BOT_TOKEN` — BotFather tomonidan berilgan token
`ADMINS` — administrator(lar) Telegram ID(lar)i (vergul bilan ajratish mumkin)

---

## ▶️ **Ishga tushirish**

Oddiy ishga tushirish:

```bash
python main.py
```

---

## 🧩 **Loyiha haqida qisqacha**

Bot foydalanuvchi bilan interaktiv muloqot qilib, quyidagi bo‘limlar orqali murojaatlarni qabul qiladi:

* 📌 Korrupsiya bilan bog‘liq xabar berish
* 📌 Qonun buzilishi haqida murojaat
* 📌 Savol va takliflar yuborish

Bot administratorlarga bildirishnoma yuboradi va murojaatlar bazada saqlanadi.

---

## 📄 **Litsenziya**

MIT License

```
Copyright (c) 2025 Shamshod
```
