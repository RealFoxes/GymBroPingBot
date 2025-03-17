# Используем официальный легковесный образ Python
FROM python:3.11-slim

# Задаём рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем необходимые библиотеки
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код бота в контейнер
COPY . .

# Команда для запуска бота
CMD ["python", "bot.py"]