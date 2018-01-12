"""Randomless just doesn't even exist here .... v2.0"""

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
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('GET ME TO RANDOM')
    bot.send_message(message.from_user.id,
                     'Be careful, some of vids are too random...',
                     reply_markup=user_markup)

@bot.message_handler(commands=['randomoro'])
def handle_text(message):
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
        import random
        answer = random.choice(("May be you will be inspired by watching this: https://www.youtube.com/watch?v=",
                                "Wow, that looks weird... https://www.youtube.com/watch?v=",
                                "It should be kind of coincidence: https://www.youtube.com/watch?v=",
                                "That's deep... https://www.youtube.com/watch?v=",
                                "If it is not the best content, I don't know what is. https://www.youtube.com/watch?v=",
                                "That's too random even for this service.. https://www.youtube.com/watch?v=",
                                "When we live in 2018, they live in 3018: https://www.youtube.com/watch?v=",
                                "Think about it: https://www.youtube.com/watch?v=",
                                "This deserves to be in trending: https://www.youtube.com/watch?v=",
                                "It looks like it is Da way to something: https://www.youtube.com/watch?v=",
                                "是的，这是中国的评论，因为为什么不呢？ https://www.youtube.com/watch?v=",
                                "Future is here, wow: https://www.youtube.com/watch?v=",
                                "Does not it illegal? https://www.youtube.com/watch?v=",
                                "If you were offended by this video, contact me by typing /help: https://www.youtube.com/watch?v=",))
        finanswer = answer + videoId
        log(message, finanswer)
        bot.send_message(message.chat.id, finanswer)

@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = """Here might be an useful content or your ad, but not this time..."""
    log(message, answer)
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['support'])
def handle_text(message):
    answer = "If you want to contact me, You know da way - @hestias"
    log(message, answer)
    bot.send_message(message.chat.id, answer)
    template_sticker_id = 'CAADAgADRC4AAuCjggcUYuBma3ILIwI'
    bot.send_sticker(message.chat.id, template_sticker_id)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    funanswer = "You printed something weird, I wont even try to understand this"
    if message.text == "GET ME TO RANDOM":
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
            import random
            answer = random.choice(("May be you will be inspired by watching this: https://www.youtube.com/watch?v=",
                      "Wow, that looks weird... https://www.youtube.com/watch?v=",
                      "It should be kind of coincidence: https://www.youtube.com/watch?v=",
                      "That's deep... https://www.youtube.com/watch?v=",
                      "If it is not the best content, I don't know what is. https://www.youtube.com/watch?v=",
                      "That's too random even for this service.. https://www.youtube.com/watch?v=",
                      "When we live in 2018, they live in 3018: https://www.youtube.com/watch?v=",
                      "Think about it: https://www.youtube.com/watch?v=",
                      "This deserves to be in trending: https://www.youtube.com/watch?v=",
                      "It looks like it is Da way to something: https://www.youtube.com/watch?v=",
                      "是的，这是中国的评论，因为为什么不呢？ https://www.youtube.com/watch?v=",
                      "Future is here, wow: https://www.youtube.com/watch?v=",
                      "Does not it illegal? https://www.youtube.com/watch?v=",
                      "If you were offended by this video, contact me by typing /help: https://www.youtube.com/watch?v=",))
            finanswer = answer + videoId
            log(message, finanswer)
            bot.send_message(message.from_user.id, finanswer)
    elif message.text == "Deus":
        answer = "Vult!"
        log(message, answer)
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, funanswer)
        log(message, funanswer)

bot.polling(none_stop=True, interval=0)
