from telegram.ext import Updater, CommandHandler

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi!")

# Create an instance of the Updater class
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the start function to handle the /start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
updater.start_polling()