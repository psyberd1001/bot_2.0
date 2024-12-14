import asyncio
import logging
from venv1.bot.handlers import start
from venv1.bot.handlers.menu import profile, about_project
from venv1.bot.handlers.menu.profile import dp, bot




async def main():
    dp.include_routers(start.router, profile.router, about_project.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

