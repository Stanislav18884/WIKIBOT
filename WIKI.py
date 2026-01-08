import telebot, wikipediaapi

wiki = wikipediaapi.Wikipedia(language='ru', user_agent='TelegramBot/1.0')
bot = telebot.TeleBot("8546269980:AAHZ9I_6nq8ehdj7_Ua0-9ahaTOD7FQ2Seo")
@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-Википедия. Спроси о чем угодно!🔮\n\n""Примеры: Компьютер, Робот, Лампа")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    try:
        query = message.text.strip()
        page = wiki.page(query)
        if page.exists():
            text = page.summary[:3000] + ("..." if len(page.summary) > 3000 else "")
            response = f"📚 {page.title}\n\n{text}\n\n🔗 {page.fullurl}"
        else:
            results = wiki.search(query)[:3]
            if results:
                suggestions = "\n".join(f"• {r}" for r in results)
                response = f"Не найдено. Попробуйте:\n{suggestions}"
            else:
                response = "Ничего не найдено. Уточните запрос."
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, "Ошибка. Попробуйте позже.")

bot.infinity_polling()
