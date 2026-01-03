# Используем официальный минимальный образ Python
FROM python:3.11-alpine

# Создаем non-root пользователя
RUN adduser -D -u 1000 appuser

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл приложения
COPY app.py .

# Меняем владельца файлов на non-root пользователя
RUN chown -R appuser:appuser /app

# Переключаемся на non-root пользователя
USER appuser

# Документируем порт
EXPOSE 8080

# Запускаем приложение
CMD ["python", "app.py"]
