import telebot 
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = types.KeyboardButton("Start")
markup.add(start_btn)
info_btn = types.KeyboardButton("Info")
markup.add(info_btn)

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
    markup.remove(types.KeyboardButton("next"))

# ℹ️ Responds to the "info" or "/info" command with more options
def Info(message):
    bot.send_message(message.chat.id, 
"""ℹ️ Information about what you need? 
1️⃣ Career options 👉 /career 
2️⃣ Skill development 👉 /skills"""
    )

# 📚 Provides descriptions and salaries for common IT careers
@bot.message_handler(func=lambda message: message.text == "/career")
def Career(message):
    bot.send_message(message.chat.id, 
"""💼 Here are some career options in IT:
1. 👨‍💻 Software Developer - Develops applications and software solutions. 💰 Salary/month: $5000
2. 📊 Data Scientist - Analyzes and interprets complex data. 💰 Salary/month: $6000
3. 🌍 Web Developer - Builds and maintains websites. 💰 Salary/month: $4500
4. ⚙️ DevOps Engineer - Manages software development and IT operations. 💰 Salary/month: $7000
5. 👔 Project Manager - Oversees IT projects and teams. 💰 Salary/month: $8000"""
    )

# 🛠️ Lists key skills for IT professions
@bot.message_handler(func=lambda message: message.text == "/skills")
def Skills(message):
    bot.send_message(message.chat.id, 
"""🛠️ Skills needed for IT careers:
1. 👨‍💻 Programming Languages (Python, Java, C++) - Essential for software development.
2. 📊 Data Analysis (SQL, Excel) - Important for data-related roles.
3. 🌍 Web Development (HTML, CSS, JavaScript) - Key for web developers.
4. ⚙️ DevOps Tools (Docker, Kubernetes) - Crucial for DevOps engineers.
5. 👔 Project Management (Agile, Scrum) - Beneficial for project managers.""")


# 🔁 Keeps the bot running and listening for new messages
bot.infinity_polling()
