from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #добавление модуля и обработчиков телеграм
import bot_settings
import datetime
import ephem
import logging   
                                                         #добавление  обработчиков python
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

def planets(bot,update):
    c_time=datetime.datetime.now()                             #привести время в нужный формат!
    current_time=c_time.strftime('%d.%m.%Y')

    input_date = update.message.text
    planet_name=input_date.split()
    if planet_name[1]=='mars':
        mars=ephem.Mars(current_time)
        planet_text=ephem.constellation(mars)
        update.message.reply_text(planet_text)
    else:
        update.message.reply_text('Не та планета')

def main():

    mybot = Updater(bot_settings.API_KEY,request_kwargs=PROXY)
    
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler('planet',planets))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))

    mybot.start_polling() #сходи и получи новые данные
    mybot.idle()
main()