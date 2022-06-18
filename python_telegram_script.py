# USE ME ON COMPUTER #

import os
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

YOUR_TOKEN_HERE = '..'
updater = Updater(YOUR_TOKEN_HERE, use_context = True)


def start  (update: Update, context: CallbackContext):
     update.message.reply_text('Welcome to your security camera, Simone!')
def help   (update: Update, context: CallbackContext):
     update.message.reply_text('Help? What!?')
def unknown(update: Update, context: CallbackContext):
     update.message.reply_text('Sorry "%s" is not a valid command' % update.message.text)

###### TODO ######
def take_image():
     pass
def take_video():
     pass
##################

def test(update: Update, context: CallbackContext):
     pic=os.path.expanduser("/home/simone/Documents/Code/MySecurityCamera/images/sample_img.jpeg")
     context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(pic,'rb'))


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('test', test))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()