import telebot 
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = types.KeyboardButton("Start")
markup.add(start_btn)




@bot.message_handler(func=lambda message: message.text == "Start" or message.text == "/start")
def handle_chat(message):
    next_btn = types.KeyboardButton("next")
    markup.add(next_btn)
    bot.send_message(message.chat.id, "Hello! I am bot that can to help you with choosing your career or profession In IT programing. To continue /next", reply_markup=markup)
    

@bot.message_handler(func=lambda message: message.text == "next" or message.text == "/next")
def handle_next(message):
    bot.send_message(message.chat.id, "Great! Let's start with some questions to understand your interests and skills. Please answer the following questions with 'yes' or 'no'.", reply_markup=markup)
    questions = [
        "Do you enjoy solving complex problems?",
        "Are you interested in working with data and analytics?",
        "Do you like creating websites or applications?",
        "Are you interested in cloud computing and DevOps?",
        "Do you enjoy managing projects and leading teams?"
    ]
    bot.send_message(message.chat.id, questions[0])
    bot.register_next_step_handler(message, process_first_answer, questions, 1, [])

def process_first_answer(message, questions, question_index, answers):
    if message.text.lower() == "yes":
        answers.append("Yes")
    elif message.text.lower() == "no":
        answers.append("No")
    else:
        bot.send_message(message.chat.id, "Please answer with 'yes' or 'no'.")
        bot.register_next_step_handler(message, process_first_answer, questions, question_index, answers)
        return

    if question_index < len(questions):
        bot.send_message(message.chat.id, questions[question_index])
        bot.register_next_step_handler(message, process_first_answer, questions, question_index + 1, answers)
    else:
        bot.send_message(message.chat.id, "Thank you for answering all the questions!")
        process_answers(message, answers)

def process_answers(message, answers):
    suggestions = []
    if answers[0] == "Yes":
        suggestions.append("Software Developer")
    if answers[1] == "Yes":
        suggestions.append("Data Analyst")
    if answers[2] == "Yes":
        suggestions.append("Web Developer")
    if answers[3] == "Yes":
        suggestions.append("DevOps Engineer")
    if answers[4] == "Yes":
        suggestions.append("Project Manager")

    if suggestions:
        bot.send_message(message.chat.id, f"Based on your answers, you might consider a career in: {', '.join(suggestions)}")
    else:
        bot.send_message(message.chat.id, "It seems like you might not be interested in IT careers. Feel free to ask for more information.")






bot.infinity_polling()