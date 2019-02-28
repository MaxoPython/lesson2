from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #добавление модуля и обработчиков телеграм

import logging                                                            #добавление  обработчиков python
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot,update):
    text ='Вызван Start!'
    logging.info (text)
    update.message.reply_text(text)

def talk_to_me(bot,update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text) 
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.last_name, update.message.chat.id, 
                 update.message.text)
    update.message.reply_text(user_text)
       
def main():
    mybot = Updater("785187042:AAGuh5KxPuU75flk04CfrZmFHubWuyqkUL8",request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    mybot.start_polling() #сходи и получи новые данные
    mybot.idle()
main()