#!/usr/bin/env python3
"""
SECRETLY Bot — отвечает на /start кнопкой открытия Mini App
Установка: pip install pyTelegramBotAPI
Запуск: python bot.py
"""

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ── НАСТРОЙКИ ──────────────────────────────────────────
BOT_TOKEN = "8716529642:AAEDU1cJagjPIwlsHLqvwgEj0o1z7SfNbFM"
APP_URL   = "https://ssknet1.github.io/SECRETLY/"  # твой GitHub Pages URL
# ───────────────────────────────────────────────────────

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="🛍 Открыть магазин SECRETLY",
            web_app=WebAppInfo(url=APP_URL)
        )
    )
    bot.send_message(
        message.chat.id,
        "☄︎ Добро пожаловать в *SECRETLY*\n\n"
        "Магазин одежды и обуви по самым лучшим ценам!.\n\n"
        "Качество · Доставка по России · Поддержка на каждом этапе\n\n"
        "Нажми кнопку ниже чтобы открыть каталог ⤵︎",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: True)
def default(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="🛍 Открыть магазин",
            web_app=WebAppInfo(url=APP_URL)
        )
    )
    bot.send_message(
        message.chat.id,
        "Используй кнопку ниже для открытия магазина 👇",
        reply_markup=keyboard
    )

print("✅ Бот запущен...")
bot.polling(none_stop=True)