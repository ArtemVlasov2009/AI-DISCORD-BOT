'''
    Модуль для роботи з Discord 

    У цьому файлі логіка нашого бота, його взаємодії з Discord сервером
'''
import discord
import dotenv, os
from .ai import get_response_from_ai

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
async def on_message(message):
    try:
        if message.author != bot_client.user:
            content = message.content
            # Отримаємо відповідь від штучного інтелекту, та відправляємо користувачу
            response = await get_response_from_ai(content)
            # Отримуємо повідомлення користувача, щоб відповісти на нього
            message_for_answer = await message.channel.fetch_message(message.id)
            # Відповідаємо на повідомлення користувача
            await message_for_answer.reply(response)
    except:
        print("Error, message:", message)