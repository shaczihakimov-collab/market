@echo off
echo 🚀 Автоматический запуск Telegram Marketplace Bot с ngrok
echo.

echo 📋 Что будет сделано:
echo 1. Настройка токена ngrok
echo 2. Запуск ngrok на порту 8000
echo 3. Получение HTTPS URL
echo 4. Обновление бота
echo 5. Запуск бота
echo.

pause

echo 🔧 Настройка ngrok...
python setup_ngrok_auto.py --auto

echo.
echo ✅ Готово! Теперь можно тестировать бота в Telegram
pause