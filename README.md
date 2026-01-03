# Веб-приложение с Nginx и Python Backend

Простое веб-приложение в Docker-контейнерах с Nginx как reverse proxy.

## Начало работы

1. **Клонируйте и перейдите в папку:**
    
   git clone https://github.com/StenElowedBay/effective_mobile.git
   cd effective_mobile

2. **Запустите приложение:**
    
   docker-compose up --build -d

3. **Проверьте работу:**
    
   curl http://localhost

Ожидаемый ответ: `Hello from Effective Mobile!`

├── backend
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
├── nginx
│   └── nginx.conf
└── README.md



## Архитектура


Пользователь → Nginx:80 → Backend:8080 (внутри сети)

- **Nginx** принимает запросы на порту 80
    
- **Backend** (Python HTTP-сервер) слушает порт 8080, доступен только внутри Docker-сети
    
- **Docker Compose** управляет сервисами и сетью
    

## Технологии

- Docker 20.10+
    
- Docker Compose 1.29+
    
- Python 3.11
    
- Nginx 1.24

## Команды управления

**Запуск:**

docker-compose up -d

**Остановка:**

docker-compose down

**Просмотр логов:**

docker-compose logs -f

**Статус сервисов:**

docker-compose ps

## Проверка работоспособности

1. Основной тест:
    
   curl http://localhost

2. Проверка в браузере:  
    Откройте `http://localhost`
    
3. Проверка healthcheck:
    
   docker-compose ps

Оба сервиса должны быть в статусе `healthy`.

## Устранение неполадок

**Если порт 80 занят:**

- Найдите процесс: `sudo lsof -i :80`
    
- Или измените порт в `docker-compose.yml`:
    
  ports:
  - "8080:80"

**Приложение не запускается:**

docker-compose logs
docker-compose down
docker-compose build --no-cache
docker-compose up -d


##  Остановка и очистка

**Остановить сервисы:**

docker-compose down

**Полная очистка:**

docker-compose down -v

---

После запуска по адресу `http://localhost` будет доступно приложение с текстом "Hello from Effective Mobile!"
