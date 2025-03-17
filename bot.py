import os
from datetime import datetime, date, time
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update

# Получаем переменные окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
START_DATE = os.getenv('START_DATE')  # формат YYYY-MM-DD

if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
    raise ValueError("Установите переменные окружения TELEGRAM_BOT_TOKEN и CHAT_ID.")

# Если START_DATE задана, пытаемся преобразовать её, иначе считаем, что стартовая дата — день первого запуска
if START_DATE:
    try:
        start_date = datetime.strptime(START_DATE, "%Y-%m-%d").date()
    except Exception as e:
        raise ValueError("START_DATE должна быть в формате YYYY-MM-DD")
else:
    start_date = date.today()

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def send_ping(context: CallbackContext):
    """Отправляет сообщение с номером дня, вычисленным на основе разницы с start_date."""
    today = date.today()
    day_counter = (today - start_date).days + 1
    if day_counter == 1:
        message = "Уговариваю Сергея пойти в зал"
    else:
        message = f"День {day_counter}: время тренироваться, Сергей!"
    try:
        context.bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Отправлено сообщение: {message}")
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

def stop_bot(update: Update, context: CallbackContext):
    """
    Если входящее сообщение от нужного чата равно "Да" (без учета регистра), останавливаем бота.
    """
    if str(update.effective_chat.id) == str(CHAT_ID):
        if update.message.text.strip().lower() == "да":
            context.bot.send_message(chat_id=CHAT_ID, text="Получил ответ 'Да'. Останавливаю бота.")
            print("Остановка бота по команде пользователя.")
            updater.stop()

def main():
    # Планирование отправки сообщений:
    # - В будние дни (Пн-Пт) в 09:00
    updater.job_queue.run_daily(send_ping, time=time(9, 0, 0), days=(0, 1, 2, 3, 4))
    # - На выходных (Сб, Вс) в 11:00
    updater.job_queue.run_daily(send_ping, time=time(11, 0, 0), days=(5, 6))
    
    # Обработчик входящих текстовых сообщений для остановки бота
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, stop_bot))
    
    # Запускаем бота (polling)
    updater.start_polling()
    print("Бот запущен. Ожидание сообщений и выполнение задач по расписанию...")
    updater.idle()

if __name__ == '__main__':
    main()
