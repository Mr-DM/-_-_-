import telebot 
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)
#Def use in bot.py the defs here for easy use and checking the code or text

def Career(message):
    bot.send_message(message.chat.id, 
"""💼 Here are some career options in IT:
1. 👨‍💻 Software Developer - Develops applications and software solutions. 💰 Salary/month: $5000
2. 📊 Data Scientist - Analyzes and interprets complex data. 💰 Salary/month: $6000
3. 🌍 Web Developer - Builds and maintains websites. 💰 Salary/month: $4500
4. ⚙️ DevOps Engineer - Manages software development and IT operations. 💰 Salary/month: $7000
5. 👔 Project Manager - Oversees IT projects and teams. 💰 Salary/month: $8000"""
    )

def Skills(message):
    bot.send_message(message.chat.id, 
"""🛠️ Skills needed for IT careers:
1. 👨‍💻 Programming Languages (Python, Java, C++) - Essential for software development.
2. 📊 Data Analysis (SQL, Excel) - Important for data-related roles.
3. 🌍 Web Development (HTML, CSS, JavaScript) - Key for web developers.
4. ⚙️ DevOps Tools (Docker, Kubernetes) - Crucial for DevOps engineers.
5. 👔 Project Management (Agile, Scrum) - Beneficial for project managers.

For more information "/more" to get additional resources and links.""")

def Info(message):
    bot.send_message(message.chat.id, 
"""ℹ️ Information about what you need? 
1️⃣ Career options 👉 /career 
2️⃣ Skill development 👉 /skills
3️⃣ Start again the conversation 👉 /start
4️⃣ For more information about IT careers 👉 /more"""
)
    
def More(message):
    bot.send_message(message.chat.id, 
"""🔍 More information:
1. programming languages: Python, Java, C++, etc - top 100 languages [https://www.bairesdev.com/blog/top-programming-languages/]\n
2. data analysis tools: SQL, Excel, R, Python [https://www.coursera.org/articles/data-analysis-tools]\n
3. web development frameworks: React, Angular, Vue.js [https://www.sencha.com/blog/web-application-development-top-frameworks/]\n
4. DevOps tools: Docker, Kubernetes, Jenkins  [https://www.redhat.com/en/topics/devops/what-is-devops]\n
5. project management methodologies: Agile, Scrum, Waterfall  [https://www.projectmanager.com/blog/project-management-methodology]\n
"""
)