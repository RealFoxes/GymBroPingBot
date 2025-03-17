import os
import time
import schedule
from telegram import Bot

# Получаем токен и id чата из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

if TELEGRAM_BOT_TOKEN is None or CHAT_ID is None:
    raise ValueError("Необходимо установить переменные окружения TELEGRAM_BOT_TOKEN и CHAT_ID.")

    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    # Глобальный счетчик дней
    day_counter = 1

    def send_ping():
        global day_counter
            # Для первого дня используем нужное сообщение
                if day_counter == 1:
                        message = "Уговариваю Сергея пойти в зал"
                            else:
                                    message = f"День {day_counter}: время тренироваться, Сергей!"
                                        
                                            try:
                                                    bot.send_message(chat_id=CHAT_ID, text=message)
                                                            print(f"Сообщение отправлено: {message}")
                                                                except Exception as e:
                                                                        print(f"Ошибка при отправке сообщения: {e}")
                                                                            
                                                                                day_counter += 1

                                                                                def schedule_jobs():
                                                                                    # Планирование:
                                                                                        # - В будние дни в 09:00
                                                                                            schedule.every().monday.at("09:00").do(send_ping)
                                                                                                schedule.every().tuesday.at("09:00").do(send_ping)
                                                                                                    schedule.every().wednesday.at("09:00").do(send_ping)
                                                                                                        schedule.every().thursday.at("09:00").do(send_ping)
                                                                                                            schedule.every().friday.at("09:00").do(send_ping)
                                                                                                                # - На выходных в 11:00 (позже, чем в будние)
                                                                                                                    schedule.every().saturday.at("11:00").do(send_ping)
                                                                                                                        schedule.every().sunday.at("11:00").do(send_ping)
                                                                                                                            print("Задачи запланированы.")

                                                                                                                            if __name__ == '__main__':
                                                                                                                                schedule_jobs()
                                                                                                                                    print("Запуск планировщика...")
                                                                                                                                        while True:
                                                                                                                                                schedule.run_pending()
                                                                                                                                                        time.sleep(30)