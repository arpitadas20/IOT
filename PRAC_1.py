import telepot
token = '123456789:syhgfligily'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())

https://api.telegram.org/bot123456789:syhgfligily/getUpdates

https://api.telegram.org/bot123456789:syhgfligily/sendMessage?chat_id=000000000&text=WeLoveIoT

import telepot
token = '123456789:syhgfligily'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
