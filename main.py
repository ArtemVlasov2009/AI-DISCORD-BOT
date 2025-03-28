'''
    Головний модуль запуску Dicord бота
'''

from modules import bot_client, TOKEN

def main():
    # Звертаємося до бота, та за допомогої run запускаємо його
    bot_client.run(TOKEN)
# Виконуємо перевірку чи є це головним файлом для запуску проекту
if __name__ == '__main__':
    main()
