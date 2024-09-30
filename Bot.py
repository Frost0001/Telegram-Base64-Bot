import telebot
import webbrowser
from telebot import types
import base64

webbrowser.open('https://t.me/kwulu')

token = input('token: ')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    btn1 = types.InlineKeyboardButton('تشفير ملف', callback_data='en')
    btn2 = types.InlineKeyboardButton('فك تشفير ملف', callback_data='de')
    btn3 = types.InlineKeyboardButton('🔰 قناة البوت', url='https://t.me/kwulu')
    xx = types.InlineKeyboardMarkup()
    xx.add(btn1)
    xx.add(btn2)
    xx.add(btn3)
    bot.reply_to(message,
                 f'مرحبًا بك عزيزي المستخدم [{name}](tg://settings)\n\n- في بوت تشفير وفك تشفير Base64\n\n- للبدا اضغط على الزر الذي يناسبك من الازرار ادناه: "\n',
                 parse_mode='markdown', reply_markup=xx)


@bot.callback_query_handler(func=lambda call: True)
def code(call):
    if call.data == 'en':
        bot.send_message(call.message.chat.id, '*أرسل الملف الآن لتشفيره لك*', parse_mode='markdown')
        bot.register_next_step_handler(call.message, en_file)
    elif call.data == 'de':
        bot.send_message(call.message.chat.id, '*أرسل الملف الآن لفك تشفيره*', parse_mode='markdown')
        bot.register_next_step_handler(call.message, de_file)


def en_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        encoded_file = base64.b64encode(downloaded_file)
        bot.send_document(message.chat.id, encoded_file)
        bot.reply_to(message, '*تم تشفير الملف بنجاح* \nصانع البوت: @Frost_0001 \n @kwulu',
                     parse_mode='markdown')
    else:
        bot.reply_to(message, 'يجب إرسال الملف لتشفيره.')


def de_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        decoded_file = base64.b64decode(downloaded_file)
        bot.send_document(message.chat.id, decoded_file)
        bot.reply_to(message, '*تم فك تشفير الملف بنجاح* \nصانع البوت: @Frost_0001 \n @kwulu',
                     parse_mode='markdown')
    else:
        bot.reply_to(message, 'يجب إرسال الملف لفك تشفيره.')


bot.polling()

# حقوق محفوظة لصانع البوت Frost | @kwulu
