import asyncio
from aiogram import Bot, Dispatcher
from Handlers import  router


async def main():
    bot = Bot(token='8111917748:AAEE6S4R5tshJoftJDRPLTQptuEKY8I8nh4')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

try:
    if __name__ == '__main__':
        asyncio.run(main())
except KeyboardInterrupt:
    print("Bot is off")