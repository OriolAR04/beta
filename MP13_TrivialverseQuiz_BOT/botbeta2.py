import telebot
from telebot import types

# Tu token del bot de Telegram
TOKEN = '7455775782:AAGAnwCVb1yitZY-dXUMflFQPeOSY4WEyyc'
bot = telebot.TeleBot(TOKEN)

'''Funció per enviar un missatge de benvinguda amb el nom de l'usuari'''
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user.first_name  # Obtén el primer nom de l'usuari
    bot.reply_to(message, f"Benvingut a TrivialverseQuiz, {user_name}! Tria una categoria per començar.")
    show_menu(message.chat.id)

'''Funció per mostrar el menú'''
def show_menu(chat_id):
    # Crea un teclat de resposta amb diverses opcions de botons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    btn_start = types.KeyboardButton('/start')
    btn_stop = types.KeyboardButton('/stop')
    btn_top = types.KeyboardButton('/top')
    btn_dlc = types.KeyboardButton('/dlc')
    btn_time = types.KeyboardButton('/time')
    btn_help = types.KeyboardButton('/help')

    # Afegir els botons al menú de text
    markup.add(btn_start, btn_stop, btn_top, btn_dlc, btn_time, btn_help)
    bot.send_message(chat_id, "Prem un botó per seleccionar una opció:", reply_markup=markup)

'''Funció per mostrar les comandes disponibles amb explicació detallada'''
@bot.message_handler(commands=['help'])
def help_command(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    help_text = (
        f"{user_name}, aquí tens les comandes disponibles i les seves funcions:\n\n"
        "/start - Inicia el bot i comença una partida\n"
        "/stop - Atura la partida actual\n"
        "/top - Mostra el rànquing de jugadors, quan estigui disponible\n"
        "/dlc - Activa continguts extres (DLC), en desenvolupament\n"
        "/time - Activa el mode de joc amb temps\n"
        "/help - Mostra aquest missatge d'ajuda\n"
    )
    bot.reply_to(message, help_text)

'''Funció per aturar la partida amb explicació detallada'''
@bot.message_handler(commands=['stop'])
def stop(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    bot.reply_to(message, f"{user_name}, has aturat la partida. Pots reiniciar-la amb /start.")

'''Funció per mostrar el rànquing de jugadors amb explicació detallada'''
@bot.message_handler(commands=['top'])
def top(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    bot.reply_to(message, f"{user_name}, el rànquing encara no està disponible. Estem treballant-hi!")

'''Funció per activar continguts extres (DLC) amb explicació detallada'''
@bot.message_handler(commands=['dlc'])
def dlc(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    bot.reply_to(message, f"{user_name}, la funcionalitat DLC encara no està disponible. Estem treballant en ella.")

'''Funció per activar el mode amb temps amb explicació detallada'''
@bot.message_handler(commands=['time'])
def time(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    bot.reply_to(message, f"{user_name}, has activat el mode amb temps. Prepara't per jugar ràpid!")

'''Funció per manejar els missatges de text i altres comandes'''
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    user_name = message.from_user.first_name  # Obtén el nom de l'usuari
    bot.reply_to(message, f"{user_name}, no entenc aquest missatge. Prova una de les comandes disponibles amb /help.")

'''Funció per gestionar les accions de botons en línia'''
@bot.callback_query_handler(func=lambda call: call.data == 'show_menu')
def callback_query(call):
    user_name = call.from_user.first_name
    commands_text = (
        f"{user_name}, aquí tens la llista de comandes disponibles:\n"
        "/start - Inicia el bot\n"
        "/stop - Atura el bot\n"
        "/top - Mostra el rànquing de jugadors\n"
        "/dlc - Activa continguts extres\n"
        "/time - Activa el mode amb temps\n"
        "/help - Mostra aquest missatge d'ajuda\n"
    )
    bot.send_message(call.message.chat.id, commands_text)
'''Inici del bot'''
print("")
print("El bot està funcionant. Prem Ctrl+C per aturar-lo.")
bot.polling()