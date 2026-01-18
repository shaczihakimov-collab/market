# Настройка ngrok для Telegram Web App

Telegram Web Apps требуют HTTPS URL. Для локальной разработки используйте ngrok.

## Установка ngrok

1. Скачайте ngrok: https://ngrok.com/download
2. Распакуйте в удобную папку
3. Зарегистрируйтесь на ngrok.com и получите токен

## Настройка

1. Авторизуйтесь в ngrok:
```bash
ngrok authtoken YOUR_TOKEN_HERE
```

2. Запустите локальный сервер:
```bash
python main.py
```

3. В новом терминале запустите ngrok:
```bash
ngrok http 8000
```

4. Скопируйте HTTPS URL из вывода ngrok (например: https://abc123.ngrok.io)

5. Обновите main.py, заменив URL:
```python
web_app=WebAppInfo(url="https://YOUR_NGROK_URL.ngrok.io/marketplace")
```

## Альтернативные решения

### 1. GitHub Pages (бесплатно)
- Загрузите marketplace.html в GitHub репозиторий
- Включите GitHub Pages
- Используйте https://username.github.io/repo/marketplace.html

### 2. Netlify (бесплатно)
- Перетащите marketplace.html на netlify.com
- Получите HTTPS URL

### 3. Vercel (бесплатно)
- Загрузите файл на vercel.com
- Получите HTTPS URL

## Быстрое решение для тестирования

Пока что бот использует https://getgems.io/ - это работает, но показывает настоящий сайт.
Для вашего кастомного маркетплейса нужен один из вариантов выше.