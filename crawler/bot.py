import os
import telebot

bot = telebot.TeleBot('895507620:AAEAnWfSX0KD0Ky4urixR5QNNm6SnffOr5o')

id_list = [
    467907961, # Luan
    ]

@bot.message_handler()
def send_password(message='-- --'):
    """-------------------------------------------------------------------------
    Método que envia json.
    -------------------------------------------------------------------------"""
    # envio json para tds da lista
    for id in id_list:
        bot.send_message(id, message)


#bot.polling()
#send_error(id_list, 'jhhjkj')
