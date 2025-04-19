from aiogram import Bot, Dispatcher, types, executor

# Новий токен бота
bot = Bot(token="7679171745:AAG2ElvAtIWTOG7WQuj7jQWTfQBXx0EUwKI")
dp = Dispatcher(bot)

# Твій Telegram ID
YOUR_TELEGRAM_ID = 6821675571

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    if message.chat.id == YOUR_TELEGRAM_ID:
        await message.reply("Привіт, Тоні! Бот активний.")
    else:
        await message.reply("Доступ заборонено.")

if __name__ == "__main__":
    executor.start_polling(dp)
