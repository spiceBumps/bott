import telebot
from telebot import types
import requests
TOKEN = '1838225591:AAEeaI9T3L_n5zQCr-stdHXGsss2qHHI-QI'

WEATHER_TOKEN = '6596f316a56103539735bd87c6246997'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start", 'weather', 'help', 'films', 'find', 'profile', 'calc', 'minus', 'multipl', 'div'])
def start_bot(message):
    if message.text.lower() == '/start':
        keyboard = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Шутеичка',callback_data='joke')
        google = types.InlineKeyboardButton('Гугле', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        question = types.InlineKeyboardButton('Вопрос!', callback_data='question')
        keyboard.add(question)
        keyboard.add(btn)
        keyboard.add(google)
        bot.send_message(message.chat.id, 'Всем привет!\nЯ новый бот!''\n \nВот короткий список моих комманд:\n/help Помощь \n/weather Погода \n/find Поиск \n/films фильмы \n/profile Профиль ', reply_markup=keyboard)
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Раздел помощи по боту \nЕсли нужна помощь или сотрудничество обращайтесь сюда: \n@bites_za_dusto')
    elif message.text.lower() == '/weather':
        bot.send_message(message.chat.id, 'Вы в разделе погода.')
        bot.send_message(message.chat.id, 'Введите название города на английском:')
        bot.register_next_step_handler(message, weather_menu)
    elif message.text.lower() == '/films':
        bot.send_message(message.chat.id, 'Здесь можно легко и быстро посмотреть фильмы в том жанре, который вам нужен')
    elif message.text.lower() == '/find':
        bot.send_message(message.chat.id, 'Поиск по разделу бота')
    elif message.text.lower() == '/profile':
        bot.send_message(message.chat.id, 'Ваш профиль')
        bot.send_message(message.chat.id, 'Я не знаю твоего имени, не мог бы ты ввести его? \nВведите имя:')
        bot.register_next_step_handler(message, name)
    elif message.text.lower() == '/calc':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        
        btn1 = types.KeyboardButton('a+b')
        btn2 = types.KeyboardButton('a-b')
        btn3 = types.KeyboardButton('a*b')
        btn4 = types.KeyboardButton('a/b')
        btn5 = types.KeyboardButton('a%b')
        btn6 = types.KeyboardButton('a**b')
        keyboard.add(btn1)
        keyboard.add(btn2)
        keyboard.add(btn3)
        keyboard.add(btn4)   
        keyboard.add(btn5)
        keyboard.add(btn6)
        bot.send_message(message.chat.id,
                         'Калькулятор! \nВыберите действие:',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, calc_choose_sum)
        bot.register_next_step_handler(message, calc_choose_minus)
        bot.register_next_step_handler(message, calc_choose_multipl)
        bot.register_next_step_handler(message, calc_choose_div)
        bot.register_next_step_handler(message, calc_choose_exponentiation)
        bot.register_next_step_handler(message, calc_choose_divv)
def calc_choose_sum(message):
    if message.text.lower() == 'a+b':
        bot.send_message(message.chat.id, 'Вы выбрали сложение.' )
        bot.send_message(message.chat.id, 'Введите два числа в одном сообщении')
        bot.register_next_step_handler(message, calc_result_sum)

def calc_result_sum(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f'Результат: \n{num1 + num2}')

def calc_choose_minus(message):
    if message.text.lower() == 'a-b':
        bot.send_message(message.chat.id, 'Вы выбрали вычитание.')
        bot.send_message(message.chat.id, 'Введите два числа в одном сообщении')
        bot.register_next_step_handler(message, calc_result_minus)

def calc_result_minus(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f'Результат: \n{num1 - num2}')


def calc_choose_multipl(message):
    if message.text.lower() == 'a*b':
        bot.send_message(message.chat.id, 'Вы выбрали умножение.')
        bot.send_message(message.chat.id, "Введите  два чилса в одном сообщении")
        bot.register_next_step_handler(message, calc_result_multipl)

def calc_result_multipl(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f'Результат: \n{num1 * num2}')


def calc_choose_div(message):
    if message.text.lower() == 'a/b':
        bot.send_message(message.chat.id, 'Вы выбрали деление')
        bot.send_message(message.chat.id, 'Введите два числа в одном сообщении')
        bot.register_next_step_handler(message, calc_result_div)

def calc_result_div(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f'Результат: \n{num1 / num2}')
    
def calc_choose_exponentiation(message):
    if message.text.lower() == 'a**b':
        bot.send_message(message.chat.id, 'Вы выбрали возведение в степень.')
        bot.send_message(message.chat.id, 'Введите два числа в одном сообщении')
        bot.register_next_step_handler(message, calc_result_exponentiation)

def calc_result_exponentiation(message):
    nums = message.text.split()
    num = int(nums[0])
    num1 = int(nums[1])
    bot.send_message(message.chat.id, f'Резульат: \n{num ** num1}')
    

def calc_choose_divv(message):
    if message.text.lower() == 'a%b':
        bot.send_message(message.chat.id, 'Вы выбрали деление в остатком.')
        bot.send_message(message.chat.id, 'Введите два числа в одном сообщении')
        bot.register_next_step_handler(message, calc_result_divv)

def calc_result_divv(message):
    nums = message.text.split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    bot.send_message(message.chat.id, f'Результат: {num1 % num2}')


@bot.message_handler(content_type = 'text')
def name (message):
    name  = message.text
    bot.send_message(message.chat.id, f'Приятно познакомиться {name}!')
    bot.send_message(message.chat.id, 'А сколько тебе лет?')
    bot.register_next_step_handler(message, age)


def age(message):
    age = message.text
    bot.send_message(message.chat.id, f'Тебе {age} лет, понятно')
    bot.send_message(message.chat.id, 'Пожалуйста скажите ваш номер:')
    bot.register_next_step_handler(message, phone_num)
                                   
def phone_num(message):
    phone_num = message.text
    bot.send_message(message.chat.id, f'Ваш номер: {phone_num}')
    bot.send_message(message.chat.id, 'Введтие название вашего города:')
    bot.register_next_step_handler(message, city)
def city(message):
    city = message.text
    bot.send_message(message.chat.id, f'Ваш город: \n{city}')
    bot.send_message(message.chat.id, 'Введите название вашего любимого(ой) фильма/игры:')
    bot.register_next_step_handler(message, film_game)
def film_game(message):
    film_game = message.text
    bot.send_message(message.chat.id, f'Твой любимый(ая) фильм/игра: \n{film_game}')
    bot.send_message(message.chat.id, 'Спасбо за эту информацию, надеюсь она будет использываться хоть когда-нибудь')
    
    
    

    
@bot.callback_query_handler(func=lambda x: x.data == 'joke')
def joke_fn(message):
    bot.send_message(message.from_user.id, 'стоят Петька и Вася \nГоворит Петька Васе:"Тсссс..."\nВася отвечает:"Что такое?"\nПетя-:"Тссссс.."\nВася-:"Да объясни что такое?"\nПетя-:"У меня комар на хую сидит."\nВася-:"Ну и что?"\nПетя-:Ну сосёт падла.')
    
    
@bot.callback_query_handler(func=lambda x: x.data == 'question')
def question_btn(message):
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Две тонны',callback_data='ansF')
    btn2 = types.InlineKeyboardButton('Один слон', callback_data='ansF')
    btn3 = types.InlineKeyboardButton('Четыре тонны', callback_data='ansT')
    keyboard.add(btn1)
    keyboard.add(btn2)
    keyboard.add(btn3)
    bot.send_message(message.from_user.id, 'Вопрос: \nCколько весит язык синего кита?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: x.data == 'ansF')
def answer1(message):
    bot.send_message(message.from_user.id, 'Неправильный ответ!')

@bot.callback_query_handler(func=lambda x: x.data == 'ansT')
def answer3(message):
    bot.send_message(message.from_user.id, 'Правильный ответ')
    
#pogoda
def weather_menu(message):
    city = message.text
    API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}'
    r = requests.get(API_URL)
    print(r.text)
    w = r.json()
    bot.send_message(message.chat.id, f'В городе: {w["name"]}')
    bot.send_message(message.chat.id, f'Температура: {w["main"]["temp"]-273.15}')
    bot.send_message(message.chat.id, f'Скорость ветра: {w["wind"]["speed"]}м/c')
    bot.send_message(message.chat.id, f'Давление: {w["main"]["pressure"]} Па' )
    bot.send_message(message.chat.id, f'Влажность: {w ["main"]["humidity"]}%')






bot.polling()