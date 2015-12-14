#!/usr/bin/env python

from telegram import Updater

import sys
import logging
import random
import urllib

root = logging.getLogger()
root.setLevel(logging.INFO)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

logger = logging.getLogger(__name__)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Please type /help for functions')

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='/turingtest, /gerrit, /halay, /icselhalay')

def turingtest(bot, update):
    texts = ["srsly mate?", "cmon dude", "what? my name is ozcan, i'm a free inhabitant", "you talking to me?"]
    bot.sendMessage(update.message.chat_id, text=texts[random.randint(0,3)])

def gerrit(bot, update):
    bot.sendMessage(update.message.chat_id, text='Try https://gerrit.libreoffice.org/ and https://bugs.documentfoundation.org/')    

def halay(bot, update):
    bot.sendMessage(update.message.chat_id, text="\o/\\o/\\o/")

def icselhalay(bot, update):
    bot.sendMessage(update.message.chat_id, text="halay icsellestiriliyor")

def echo(bot, update):
    # slap x => kicking @x from group.
    if "slap" in update.message.text:
        texts = ['Kicking @'+update.message.text.split(" ")[1]+' from group.']
        bot.sendMessage(update.message.chat_id, text=texts[0])
    # google x => LMGTFY
    elif "google" in update.message.text:
    	search = "http://lmgtfy.com/?q=" + urllib.quote_plus(update.message.text.replace("google",""))
	bot.sendMessage(update.message.chat_id, text=search)
    else:
        bot.sendMessage(update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater("KEY")

    dp = updater.dispatcher

    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", help)
    dp.addTelegramCommandHandler("gerrit", gerrit)
    dp.addTelegramCommandHandler("turingtest", turingtest)
    dp.addTelegramCommandHandler("halay", halay)
    dp.addTelegramCommandHandler("icselhalay", icselhalay)
    
    dp.addTelegramMessageHandler(echo)

    dp.addErrorHandler(error)
    updater.start_polling(timeout=5)
    updater.idle()

if __name__ == '__main__':
    main()
