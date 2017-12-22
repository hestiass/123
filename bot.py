"""Randomless just doesn't even exist here"""

import telebot
import json
import urllib.request
import string

bot = telebot.TeleBot("409046638:AAFTexgRRmdcbqVGLgXhaGfB__Akcrf4ynQ")

print(bot.get_me())

def log(message, answer):
    print("\n -----")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, """So, this bot will try to generate something...""")
    user_markup = telebot.types.ReplyKeyboardMarkup(False, False)
    user_markup.row('GET ME TO RANDOM')
    bot.send_message(message.from_user.id,
                     'Be careful, some of vids are too random...',
                     reply_markup=user_markup)

@bot.message_handler(commands=['randomoro'])
def handle_text(message):
    answer = "It's cool that you descided to use slash instead of buttons, but I think it's not worth it..."
    log(message, answer)
    bot.send_message(message.from_user.id, answer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = """Here might be an useful content or your ad, but not this time..."""
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "You printed something weird, I wont even try to understand this"
    if message.text == "/support":
        answer = "plz text me smt right here - @hestias"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "Deus":
        answer = "Vult!"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    elif message.text == "GET ME TO RANDOM":
        import random
        count = 1
        API_KEY = 'AIzaSyDN51PGJ1NWEXlg1cUNrmmf42ayUMkQx4Y'
        random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(
            API_KEY, count, random)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        results = json.loads(data.decode(encoding))
        for data in results['items']:
            videoId = (data['id']['videoId'])
            print(videoId)
            answer = "May be you will be inspired by watching this: https://www.youtube.com/watch?v=" + videoId
            log(message, answer)
            bot.send_message(message.from_user.id, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)

bot.polling(none_stop=True, interval=0)