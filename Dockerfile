# Используем официальный образ Python (легковесный вариант)
FROM python:3.11-slim

# Задаём рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код в контейнер
COPY . .

# Команда для запуска бота
CMD ["python", "bot.py"]
