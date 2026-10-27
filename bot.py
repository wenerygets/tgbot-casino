"""
🎰 Telegram Casino Bot
Запуск: python bot.py
Требования: pip install aiogram==3.* aiohttp
"""

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    WebAppInfo, MenuButtonWebApp, BotCommand
)

BOT_TOKEN = "9011082336:AAGOmX51-RfhE25o1zpbiK8C-vhmHiZWsmg"

# URL твоего Mini App (после деплоя замени на реальный)
WEBAPP_URL = "http://153.80.249.114"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    """Приветствие и кнопка запуска Mini App"""
    text = (
        "🎁💎 Выиграйте NFT-подарки мечты!\n\n"
        "Вам доступен бесплатный кейс, а также рулетка, краш, PvP, слоты, яйца и апгрейд."
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🎮 Играть",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )],
    ])

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")


@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    text = (
        "🎰 <b>Gift Roulette Casino — Помощь</b>\n\n"
        "<b>Команды:</b>\n"
        "/start — Главное меню\n"
        "/balance — Твой баланс монет\n"
        "/daily — Ежедневный бонус\n"
        "/top — Топ игроков\n\n"
        "<b>Как играть:</b>\n"
        "1. Открой казино кнопкой в /start\n"
        "2. Крути рулетку — трать монеты\n"
        "3. Выигрывай призы и монеты!\n\n"
        "💡 Каждый день получай бесплатные монеты через /daily"
    )
    await message.answer(text, parse_mode="HTML")


@dp.message(Command("balance"))
async def balance_cmd(message: types.Message):
    # В реальном боте здесь запрос к БД
    user_id = message.from_user.id
    await message.answer(
        f"💰 <b>Твой баланс</b>\n\n"
        f"🪙 Монеты: <b>1000</b>\n"
        f"🎁 Подарков выиграно: <b>0</b>\n"
        f"🎰 Крутов рулетки: <b>0</b>\n\n"
        f"<i>Используй /daily для ежедневного бонуса!</i>",
        parse_mode="HTML"
    )


@dp.message(Command("daily"))
async def daily_cmd(message: types.Message):
    await message.answer(
        "🎁 <b>Ежедневный бонус!</b>\n\n"
        "✅ Ты получил <b>+500 монет</b>!\n\n"
        "Возвращайся завтра за новым бонусом 🎰",
        parse_mode="HTML"
    )


@dp.callback_query(lambda c: c.data == "balance")
async def balance_callback(callback: types.CallbackQuery):
    await callback.answer()
    await balance_cmd(callback.message)


@dp.callback_query(lambda c: c.data == "leaderboard")
async def leaderboard_callback(callback: types.CallbackQuery):
    await callback.answer()
    text = (
        "🏆 <b>Топ игроков</b>\n\n"
        "1. 🥇 @player1 — 50,000 монет\n"
        "2. 🥈 @player2 — 35,000 монет\n"
        "3. 🥉 @player3 — 28,000 монет\n"
        "4. @player4 — 15,000 монет\n"
        "5. @player5 — 9,000 монет\n\n"
        "<i>Играй больше, чтобы попасть в топ!</i>"
    )
    await callback.message.answer(text, parse_mode="HTML")


async def set_bot_commands():
    """Устанавливает команды бота в меню"""
    commands = [
        BotCommand(command="start", description="🎰 Главное меню"),
        BotCommand(command="balance", description="💰 Мой баланс"),
        BotCommand(command="daily", description="🎁 Ежедневный бонус"),
        BotCommand(command="help", description="❓ Помощь"),
    ]
    await bot.set_my_commands(commands)


async def set_menu_button():
    """Кнопка Mini App в меню ввода"""
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="🎰 Казино",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )


async def main():
    logger.info("Бот запускается...")
    await set_bot_commands()
    # await set_menu_button()  # Раскомментируй после деплоя фронтенда
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
