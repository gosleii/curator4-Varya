import telebot

bot = telebot.TeleBot('6926754912:AAHs46Iz2SVjQhcPsve8NNLkEys7cN93IHg')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! Хочешь дам совет? Жми любую цифру от 1 до 8. Та, что ты выбрал - твой совет на сегодня)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['1'])
def main(message):
    bot.send_message(message.chat.id, '*Стремитесь не к успеху, а к ценностям, которые он дает.* /nАльберт Эйнштейн',
                     parse_mode='Markdown')


@bot.message_handler(commands=['2'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно.* /nАльберт Эйнштейн',
                     parse_mode='Markdown')


@bot.message_handler(commands=['3'])
def main(message):
    bot.send_message(message.chat.id, '*Надо любить жизнь больше, чем смысл жизни.* /nФёдор Достоевский',
                     parse_mode='Markdown')


@bot.message_handler(commands=['4'])
def main(message):
    bot.send_message(message.chat.id, '*80% успеха - это появиться в нужном месте в нужное время.* /nВуди Аллен',
                     parse_mode='Markdown')


@bot.message_handler(commands=['5'])
def main(message):
    bot.send_message(message.chat.id, '* Жизнь - это то, что с тобой происходит, пока ты строишь планы.* /nДжон Леннон',
                     parse_mode='Markdown')


@bot.message_handler(commands=['6'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Вы никогда не пересечете океан, если не наберетесь мужества потерять берег из виду.* /nХристофор Колумб',
                     parse_mode='Markdown')


@bot.message_handler(commands=['7'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Идите уверенно по направлению к мечте. Живите той жизнью, которую вы сами себе придумали.* /nГенри Дэвид Торо',
                     parse_mode='Markdown')


@bot.message_handler(commands=['8'])
def main(message):
    bot.send_message(message.chat.id,
                     '* Успех — это способность идти от поражения к поражению, не теряя оптимизма.* /nУинстон Черчилль',
                     parse_mode='Markdown')


bot.infinity_polling()