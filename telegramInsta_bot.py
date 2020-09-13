import telepot
from instaFollowers import getFollowers, getAssholes, getNewOnes
from datetime import date, timedelta
import os


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        usr_id = bot.getChat(chat_id)
        txt = msg['text']

        if '/start' in txt:
            bot.sendMessage(chat_id, 'Here I am')

        elif '/unfollowers' in txt:
            assholes = getAssholes(yesterdayList, todayList)
            message = "Unfollowers:\n"
            for i in assholes:
                message = message +i+"\n"
            bot.sendMessage(chat_id, '{}'.format(message))
            
        elif '/new_followers' in txt:
            newOnes = getNewOnes(yesterdayList, todayList)
            message = "New followers:\n"
            for i in newOnes:
                message = message +i+"\n"
            bot.sendMessage(chat_id, '{}'.format(message))

        elif '/update' in txt:
            message = str(date) + "\n\nNEW ONES: \n"
            newOnes = getNewOnes(yesterdayList, todayList) #getting new followers
            for i in newOnes:
                message = message +i+"\n"
            message = message +" \n\n"

            message = message +"ASSHOLES: \n"
            assholes = getAssholes(yesterdayList, todayList) #getting unfollowers
            for i in assholes:
                message = message +i+"\n"
                        
            bot.sendMessage(chat_id, '{}'.format(message))

            #removing old list & saving new one
            os.remove(yesterday)
            os.rename(today, yesterday)
            print("Files updated")
           



date = date.today()
today = str(date)+".txt"
yesterday = "yesterday.txt"
#yesterday = str(date - timedelta(days = 1))+".txt"
getFollowers(today)
with open(yesterday) as y:
    yesterdayList = y.read().splitlines()
    
with open(today) as t:
    todayList = t.read().splitlines()


TOKEN = '1028321692:AAHkYyXuITnM9jVhFZGw4kOSpj8SVwyxFfI'

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)
response = bot.getUpdates()



import time
while 1:
    time.sleep(10)