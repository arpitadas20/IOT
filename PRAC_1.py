import telepot
token = '1291907185:AAHvb59oPAOfwDIbMLxDkU4YYbGzvQDquss'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())

https://api.telegram.org/bot1291907185:AAHvb59oPAOfwDIbMLxDkU4YYbGzvQDquss/getUpdates

https://api.telegram.org/bot1291907185:AAHvb59oPAOfwDIbMLxDkU4YYbGzvQDquss/sendMessage?chat_id=1089788663&text=WeLoveIoT

import telepot
token = '1291907185:AAHvb59oPAOfwDIbMLxDkU4YYbGzvQDquss'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
