#import logging
import os
from telegram import Update
from telegram.ext import Updater, CallbackContext, Updater, Filters, CommandHandler, MessageHandler


# Validate we have the required token set
bot_token = os.environ.get('TOKEN')
assert bot_token, "I can't work without a token. Please set the TOKEN environment variable to the value shared by @BotFather"


updater = Updater(token=bot_token)

# Print a message to the screen when something relevant happens. (Useful when something doesn't go as expected)
# logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    """Say hi to the user"""
    the_bot = context.bot
    chat_id = update.effective_chat.id
    user_name = update.effective_user.name
    the_bot.send_message(chat_id=chat_id, text=f"👋 Hi {user_name}, i'm a bot 🤖")


def reverseit(update: Update, context: CallbackContext):
    """Reverse sent message"""
    the_bot = context.bot
    chat_id = update.effective_chat.id
    original_message = update.effective_message.text
    reversed_message = original_message[::-1]
    the_bot.send_message(chat_id=chat_id, text=reversed_message)


# Link our function to the /start command so its invoked when users type /start
start_handler = CommandHandler('start', start)
reverse_handler = MessageHandler(Filters.text & (~Filters.command), reverseit)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(reverse_handler)

# Start listening to telegram messages from users
print("The bot has started 🚀 🌕")
updater.start_polling()