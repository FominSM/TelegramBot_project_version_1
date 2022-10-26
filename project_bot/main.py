# Прикрутить бота к задачам с предыдущего семинара:

# Создать калькулятор для работы с рациональными и комплексными
# числами, организовать меню, добавив в неё систему логирования

# Создать телефонный справочник с возможностью импорта и экспорта
# данных в нескольких форматах.




from telebot import TeleBot, types
import emoji

 
bot = TeleBot('5688493072:AAFpgPLPRZKJ9VxiAqCSXu5S8IJ2CXHKycE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    calc = types.KeyboardButton(f'Калькулятор {emoji.emojize(":abacus:")}')
    telephone_directory = types.KeyboardButton(f'Cправочник {emoji.emojize(":telephone:")}')
    markup.add(calc, telephone_directory)
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, '
                    'приветствую тебя! Я тестовый бот и могу выполнять только '
                    f'2 операции, предствленные ниже, выбери же одну из них {emoji.emojize(":anxious_face_with_sweat:")}', 
                    reply_markup=markup)



# @bot.message_handler(commands=['start'])
# def start(message):
#     user_hello = f'Добро пожаловать, {message.from_user.first_name} !' 
#     bot.send_message(message.chat.id, user_hello)


@bot.message_handler(content_types=['text'])
def get_user_txt(message):
    if message.text == f'Калькулятор {emoji.emojize(":abacus:")}':
        bot.send_message(message.chat.id, 'Calc')
    elif message.text == f'Cправочник {emoji.emojize(":telephone:")}':
        bot.send_message(message.chat.id, 'Phone')
    else: bot.send_message(message.chat.id, emoji.emojize(":face_with_raised_eyebrow:"))


bot.polling()
























 
 
# def summator(text):
#     lst = text.split()
#     if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
#         return str(int(lst[0]) + int(lst[1]))
#     return 'Это некорректный запрос'
 
 
# @bot.message_handler(commands=['log'])
# def hello(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id,
#                      text='Лог программы\newcoiywgecowegcouwefoyewfov')
#     bot.send_document(chat_id=msg.from_user.id, document=open('TestBot.log', 'rb'))
 
 
# @bot.message_handler(content_types=['document'])
# def hello(msg: telebot.types.Message):
#     file = bot.get_file(msg.document.file_id)
#     downloaded_file = bot.download_file(file.file_path)
#     with open(msg.document.file_name, 'wb') as f_out:
#         f_out.write(downloaded_file)
 
 
# @bot.message_handler(commands=['help'])
# def help_command(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text="Справка")
 
 
# @bot.message_handler(commands=['summator'])
# def help_command(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
#     bot.register_next_step_handler(callback=sum_items, message=msg)
 
# def sum_items(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=summator(msg.text))
 
 
# @bot.message_handler()
# def echo(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text="Вы ввели:")
 
 
# bot.polling()






















# from telebot import TeleBot

# bot = TeleBot('5688493072:AAFpgPLPRZKJ9VxiAqCSXu5S8IJ2CXHKycE')

# def summato_(text):
#     lst = text.split()
#     if len(lst) == 2 and lst[0].isdigit() and lst[1].isdigit():
#         return str(int(lst[0]) + int(lst[1]))
#     else: return 'Invalid sintaxis'


# @bot.message_handler()
# def echo(msg):
#     bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислалииииии: {summato_(msg.text)}')

# bot.polling()