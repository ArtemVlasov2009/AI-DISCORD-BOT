'''
    Модуль для роботи з API OpenAI

    У цьому файлі логіка нашого бота, взаємодії бота з сервером OpenAI. Для формування відповіді від штучного інтелекта 
'''
import openai
import dotenv, os

# Застосовуємо dotenv для того щоб сховати OPEN_AI_SECRET_KEY (наш ключ апі)
dotenv.load_dotenv()
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")

# Створюємо клієнта для взаємодії з API штучного інтелекту
client_openai = openai.AsyncOpenAI(api_key = OPENAI_SECRET_KEY)

# Створюємо асинхронну функцію для отримання відповіді від штучного інтелекту
async def get_response_from_ai(question: str):
    # Налаштовуємо модель для відповіді
    response = await client_openai.chat.completions.create(
        model = "gpt-4o-mini", # Вибираємо модель штучного інтелекту
        messages = [{
            "role": "user", # Ставимо роль звичайного користувача
            "content": question, # Відповідаємо на питання користувача
        }],
    )
    # Повертаємо відповідь від штучного інтелекту за 0 айді
    return response.choices[0].message.content