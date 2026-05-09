from telegram.ext import Application, Updater, CommandHandler, CallbackContext, MessageHandler, filters
from telegram import Update, ForceReply
import datetime

async def start(update=Update,context=CallbackContext):
    await update.message.reply_text(f"Hi {update.message.from_user.full_name}")

async def echo(update: Update, context:CallbackContext):
    await update.message.reply_text(update.message.text)

async def time(update: Update, context: CallbackContext):
    await update.message.reply_text(datetime.datetime.strftime(datetime.datetime.now(),"%d %B %Y %H:%M:%S"))

async def help(update: Update, context: CallbackContext):
    await update.message.reply_html(
        "test telegram bot\n\n" +
        "/start - to start the bot\n" +
        "/help - to get help\n" +
        "/time - get current date and time\n",
        reply_markup=ForceReply(selective=True)
    )

def main():
    application = Application.builder().token("TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help",help))
    application.add_handler(CommandHandler("time",time))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()