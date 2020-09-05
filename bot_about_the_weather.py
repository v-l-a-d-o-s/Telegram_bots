import telebot
import urllib2
from bs4 import BeautifulSoup
html=urllib2.urlopen('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D1%80%D0%BE%D0%BF%D0%B8%D0%B2%D0%BD%D0%B8%D1%86%D0%BA%D0%B8%D0%B9/10-%D0%B4%D0%BD%D0%B5%D0%B9')
soup = BeautifulSoup(html,'html.parser')

token=""
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['weather'])
def handle_text(message):
        markup=telebot.types.ReplyKeyboardMarkup(True,False)
        markup.row('today','tomorrow')
        markup.row('week ','10 days')
        bot.send_message(message.chat.id, "Weather", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text=='today':
        div=soup.find('div', id='bd1') 
        bot.send_message(300867545,div.text)
        
    if message.text=='tomorrow':
        div=soup.find('div', id='bd2') 
        bot.send_message(300867545,div.text)
        
    if message.text=='week':
            my_list=['bd1','bd2','bd3','bd4','bd5','bd6','bd7']
            for item in my_list:
                    div=soup.find('div', id=item)
                    bot.send_message(300867545,div.text)
                    
    if message.text=='10 days':
            my_list=['bd1','bd2','bd3','bd4','bd5','bd6','bd7','bd8','bd9','bd10']
            for item in my_list:
                    div=soup.find('div', id=item)
                    bot.send_message(300867545,div.text)

bot.polling(none_stop=True,interval=0)
