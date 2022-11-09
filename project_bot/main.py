import telebot, emoji, time
from telebot import types

bot = telebot.TeleBot('Your TOKEN')

with open('project_bot/logfile.txt', 'a', encoding="utf-8") as f_log:
    local_time = time.ctime(time.time()).split()[3]
    print(local_time, 'Бот запущен', file=f_log)
 
def do_log(message, user_id):
    with open('project_bot/logfile.txt', 'a', encoding="utf-8") as f_log:
        local_time = time.ctime(time.time()).split()[3]
        print(local_time, f'Пользователь ({user_id}) выполнил операцию: {message}', file=f_log)
 

value = ''
old_value = ''
user_id = ''

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('C', callback_data='C'),
             telebot.types.InlineKeyboardButton('<=', callback_data='<='),
             telebot.types.InlineKeyboardButton('/', callback_data='/'),
             telebot.types.InlineKeyboardButton('*', callback_data='*')
             )

keyboard.row(telebot.types.InlineKeyboardButton('7', callback_data='7'),
             telebot.types.InlineKeyboardButton('8', callback_data='8'),
             telebot.types.InlineKeyboardButton('9', callback_data='9'),
             telebot.types.InlineKeyboardButton('-', callback_data='-')
             )

keyboard.row(telebot.types.InlineKeyboardButton('4', callback_data='4'),
             telebot.types.InlineKeyboardButton('5', callback_data='5'),
             telebot.types.InlineKeyboardButton('6', callback_data='6'),
             telebot.types.InlineKeyboardButton('+', callback_data='+')
             )

keyboard.row(telebot.types.InlineKeyboardButton('1', callback_data='1'),
             telebot.types.InlineKeyboardButton('2', callback_data='2'),
             telebot.types.InlineKeyboardButton('3', callback_data='3'),
             telebot.types.InlineKeyboardButton(',', callback_data='.')
             )

keyboard.row(telebot.types.InlineKeyboardButton('(', callback_data='('),
             telebot.types.InlineKeyboardButton('0', callback_data='0'),
             telebot.types.InlineKeyboardButton(')', callback_data=')'),
             telebot.types.InlineKeyboardButton('=', callback_data='=')
             )

keyboard.row(telebot.types.InlineKeyboardButton('J', callback_data='J'))

@bot.message_handler(commands = ['start'] )
def getmessage(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, '
                    'приветствую тебя! Я тестовый бот-аля калькулятор и могу выполнять различные '
                    f'арифметические операции, как с рациональными числами, '
                    'так и с комплексными, если про существование вторых услышал только сейчас, '
                    f'то лучше ознакомься с тем, что это такое и с чем их едят, после этого '
                    'ты поймешь зачем в калькуляторе кнопка "J", и не в коем случае не пиши мне '
                    f'в личные сообщения, все понял? приступим? {emoji.emojize(":anxious_face_with_sweat:")}'
                    f'{emoji.emojize(":backhand_index_pointing_down:")}'
                    )

    global user_id
    user_id = message.from_user.id
    if value == '':
        bot.send_message(message.from_user.id, "Well, let's start counting?", reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global value, old_value
    data = query.data

    if data == 'C': value = ''
    elif data == '(': value += '(' 
    elif data == ')': value +=')' 
    elif data == '<=': value = value[:-1]
    elif data == '=':
        try:
            arithmetic_expression = value
            value = str(eval(value))
            arithmetic_expression += f' = {value}'
        except:
            value = 'Ошибка!'
            arithmetic_expression += f' = {value}'
        finally:
            do_log(arithmetic_expression, user_id)
    else:
        if data in '+-/*': value += f' {data} '
        else: value += data

    if value != old_value:
        if value == '': bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, 
                                              text="0", reply_markup=keyboard)
        else: bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, 
                                    text=value, reply_markup=keyboard)

    old_value = value
    if value == 'Ошибка!': value = ''


@bot.message_handler()
def ge(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, '
                    f'работой строго с красивыми кнопками, бро {emoji.emojize(":face_with_symbols_on_mouth:")}')

bot.polling(none_stop=False, interval=0)
