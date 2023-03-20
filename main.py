import logging

from telegram.ext import Application

from settings import BOT_TOKEN

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
