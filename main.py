import asyncio
import logging
import aiogram
import aiogram.filters
import environ

env = environ.Env()
env.read_env()
logging.basicConfig(level=logging.INFO, filename="")
bot = aiogram.Bot(token=env.str("BOT_TOKEN"))
dispatcher = aiogram.Dispatcher()


@dispatcher.message(aiogram.filters.command.Command("start"))
async def command_start(message: aiogram.types.Message):
    await message.answer("Привет, как жизнь!")


@dispatcher.message(aiogram.filters.command.Command("iloveyou"))
async def command_iloveyou(message: aiogram.types.Message):
    await message.answer(
        "Любовь это наш непроизвольный ответная реакция на добро, если мы добродетельный! Так что взаимно)"
    )


async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
