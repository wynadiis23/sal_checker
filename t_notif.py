#import telegram
import configparser
import os
import requests


def notify_ending(application_path, message, token, t_ch_id):
    # this line is for read configuration file. Please set your db toko root dir on the config.ini file.
    # config = configparser.ConfigParser()
    # path_config = os.path.join(application_path, 'config.ini')
    # t_info = config['t_notif']
    token = token
    chat_id = t_ch_id    
    #bot = telegram.Bot(token=token)
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={t_ch_id}&text={message}"
    #a = bot.sendMessage(chat_id=chat_id, text=message)
    requests.get(url).json() # this sends the message
    
    #a = bot.sendMessage(chat_id=chat_id, text=message)