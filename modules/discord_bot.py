'''
    Модуль для роботи з Discord 

    У цьому файлі логіка нашого бота, його взаємодії з Discord сервером
'''
import discord
import dotenv, os

# Застосовуємо модуль dotenv, для того щоб зробити не видимою нашу змінну TOKEN
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

# Ставимо стандартні права для бота, та також даємо можливість боту читати повідомлення
intents = discord.Intents.default()
intents.message_content = True

# Створюємо самого бота
bot_client = discord.Client(intents= intents)

# Викликаємо бота та звертаємося до його події
@bot_client.event
# Створюємо асинхронну функцію яка буде виводити повідомлення про те що бот запущено
async def on_ready():
    print(f"Бот {bot_client.user} запущено")

# Викликаємо бота та звертаємося до його події 
@bot_client.event
# Створюємо асинхронну функцію яка буде виводити повідомлення які надійшли від користувачів
async def on_message(message):
    # Використовуємо конструкцію try except для того щоб вивести помилку якщо вона виникне
    try:
        # Робимо перевірку через умову чи повідомлення не від бота
        if message.author != bot_client.user:
            content = message.content
            # Виводимо повідомлення яке надійшло від користувача
            await message.channel.send(content)
    except:
        print("error")