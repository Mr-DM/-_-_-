import telebot 
from config import TOKEN
from telebot import types
from logic import *

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = types.KeyboardButton("Start")
markup.add(start_btn)
info_btn = types.KeyboardButton("Info")
markup.add(info_btn)
Career_btn = types.KeyboardButton("Career")
markup.add(Career_btn)
Skills_btn = types.KeyboardButton("Skills")
markup.add(Skills_btn)


# 💬 Handles the /start or "Start" message from the user
# Introduces the bot and shows the "next" button
@bot.message_handler(func=lambda message: message.text == "Start" or message.text == "/start")
def handle_chat(message):
    next_btn = types.KeyboardButton("next")
    markup.add(next_btn)
    bot.send_message(
        message.chat.id, 
        "👋 Hello! I am a bot that can help you choose your career or profession in IT programming 👨‍💻💡. To continue, type /next or press the 'next' button ⏭️", 
        reply_markup=markup
    )

# ❓ Starts the career quiz when user sends /next or "next"
# Sends first question and prepares to collect answers
@bot.message_handler(func=lambda message: message.text == "next" or message.text == "/next")
def handle_next(message):
    bot.send_message(
        message.chat.id, 
        "✅ Great! Let's start with some questions to understand your interests and skills. Please answer the following questions with 'yes' or 'no' 🙋‍♂️🙋‍♀️", 
        reply_markup=markup
    )
    questions = [
        "🧠 Do you enjoy solving complex problems?",
        "📊 Are you interested in working with data and analytics?",
        "🌐 Do you like creating websites or applications?",
        "☁️ Are you interested in cloud computing and DevOps?",
        "🗂️ Do you enjoy managing projects and leading teams?"
    ]
    bot.send_message(message.chat.id, questions[0])
    bot.register_next_step_handler(message, process_first_answer, questions, 1, [])

# 🔁 Recursively handles each answer in the quiz
# Validates the input and proceeds to next question
def process_first_answer(message, questions, question_index, answers):
    if message.text.lower() == "yes":
        answers.append("Yes")
    elif message.text.lower() == "no":
        answers.append("No")
    else:
        bot.send_message(message.chat.id, "❗ Please answer with 'yes' or 'no'.")
        bot.register_next_step_handler(message, process_first_answer, questions, question_index, answers)
        return

    if question_index < len(questions):
        bot.send_message(message.chat.id, questions[question_index])
        bot.register_next_step_handler(message, process_first_answer, questions, question_index + 1, answers)
    else:
        bot.send_message(message.chat.id, "🎉 Thank you for answering all the questions!")
        process_answers(message, answers)
    markup.add(info_btn, Career_btn, Skills_btn)

# 🧠 Analyzes user's answers and suggests possible IT careers
# Sends back results based on what the user answered "Yes" to
def process_answers(message, answers):
    suggestions = []
    if answers[0] == "Yes":
        suggestions.append("👨‍💻 Software Developer")
    if answers[1] == "Yes":
        suggestions.append("📈 Data Analyst")
    if answers[2] == "Yes":
        suggestions.append("🌍 Web Developer")
    if answers[3] == "Yes":
        suggestions.append("⚙️ DevOps Engineer")
    if answers[4] == "Yes":
        suggestions.append("👔 Project Manager")

    if suggestions:
        bot.send_message(message.chat.id, f"🚀 Based on your answers, you might consider a career in: {', '.join(suggestions)}")
    else:
        bot.send_message(message.chat.id, "🤔 It seems like you might not be interested in IT careers. Feel free to ask for more information 💬.")

# ℹ️ Responds to the "info" or "/info" command with more options
@bot.message_handler(func=lambda message: message.text == "Info" or message.text == "/info")
def handle_info(message):
    Info(message)   

# 📚 Provides descriptions and salaries for common IT careers
@bot.message_handler(func=lambda message: message.text == "/career" or message.text == "Career")
def handle_career(message):
    Career(message)
# 🛠️ Lists key skills for IT professions
@bot.message_handler(func=lambda message: message.text == "/skills" or message.text == "Skills")
def handle_skills(message):
    Skills(message)

@bot.message_handler(func=lambda message: message.text == "/more" or message.text == "More")
def handle_more(message):
    More(message)
# 🔁 Keeps the bot running and listening for new messages
bot.infinity_polling()
