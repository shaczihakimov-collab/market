#!/usr/bin/env python3
"""
Telegram Marketplace Bot - Getgems
Простой бот для торговли на маркетплейсе Getgems
"""

import logging
import threading
import http.server
import socketserver
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, MenuButtonWebApp, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Конфигурация бота
BOT_TOKEN = "8535517286:AAECqvGpe9fdRfori0SL98g3MK7jnfVvu6o"
WEB_SERVER_PORT = 8000
# GitHub Pages URL
WEBAPP_URL = "https://shaczihakimov-collab.github.io/market/"

# Приветственное сообщение
WELCOME_MESSAGE = """Это бот Getgems — через него можно торговать на нашем маркетплейсе прямо в мини-аппе Telegram. Это самый удобный способ продавать и покупать Telegram Подарки с нулевой комиссией, а также Юзернеймы и Анонимные Номера с комиссией всего 1%. 🎯

💡 С помощью этого бота можно делиться своими NFT в чатах. Просто отправьте сюда адрес вашего TON-кошелька — после успешной привязки начните набирать в любой переписке @getgemsnftbot. Активируется inline-режим, и Вы сможете отправлять свои NFT прямо в чаты!"""

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class MarketplaceHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Обрабатываем корневой путь
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/marketplace':
            self.path = '/getgems_marketplace.html'
        
        # Если есть параметр ngrok-skip-browser-warning, убираем его из пути
        if '?ngrok-skip-browser-warning=' in self.path:
            self.path = self.path.split('?')[0]
            if self.path == '/':
                self.path = '/getgems_marketplace.html'
            elif self.path == '/marketplace':
                self.path = '/getgems_marketplace.html'
        
        try:
            # Читаем файл
            file_path = self.path[1:] if self.path.startswith('/') else self.path
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Отправляем ответ с правильными заголовками
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('ngrok-skip-browser-warning', 'any')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.end_headers()
            
            self.wfile.write(content)
            
        except FileNotFoundError:
            self.send_error(404, "File not found")
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
    
    def log_message(self, format, *args):
        # Отключаем логи для чистоты вывода
        return


def start_web_server():
    """Запуск веб-сервера для маркетплейса"""
    handler = MarketplaceHandler
    
    with socketserver.TCPServer(("", WEB_SERVER_PORT), handler) as httpd:
        print(f"🌐 Веб-сервер маркетплейса запущен на порту {WEB_SERVER_PORT}")
        httpd.serve_forever()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    # Создание клавиатуры с навигационными кнопками
    keyboard = []
    
    # Кнопка для открытия маркетплейса
    keyboard.append([InlineKeyboardButton(
        "🎁 Открыть Маркетплейс", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )])
    
    # Обычные кнопки для Numbers и Usernames
    keyboard.append([InlineKeyboardButton("📱 Торговать Telegram Numbers", callback_data="numbers")])
    keyboard.append([InlineKeyboardButton("👤 Торговать Telegram Usernames", callback_data="usernames")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправка приветственного сообщения с кнопками
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=reply_markup
    )


async def marketplace_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /marketplace"""
    keyboard = [[InlineKeyboardButton(
        "🎁 Открыть NFT Маркетплейс", 
        web_app=WebAppInfo(url=WEBAPP_URL)
    )]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🏪 Добро пожаловать в NFT маркетплейс Getgems!\n\n"
        "Здесь вы можете:\n"
        "• Покупать и продавать уникальные NFT\n"
        "• Просматривать коллекции\n"
        "• Добавлять в избранное\n"
        "• Управлять корзиной\n\n"
        "Нажмите кнопку ниже для входа в маркетплейс:",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /help"""
    help_text = """
🤖 **Команды бота:**

/start - Главное меню
/marketplace - Открыть NFT маркетплейс
/help - Показать эту справку

🎁 **Функции:**
• Торговля Telegram подарками (0% комиссия)
• Торговля юзернеймами и номерами (1% комиссия)
• NFT маркетплейс с коллекциями
• Поиск и фильтры
• Корзина и избранное

💡 **Как пользоваться:**
1. Нажмите "Открыть Маркетплейс"
2. Просматривайте NFT коллекции
3. Добавляйте в корзину понравившиеся предметы
4. Используйте поиск и фильтры

🔗 **Поддержка:** @getgemsnftbot
    """
    
    await update.message.reply_text(help_text, parse_mode='Markdown')


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик нажатий на кнопки"""
    query = update.callback_query
    await query.answer()
    
    if query.data == "numbers":
        await query.edit_message_text(
            "📱 **Торговля Telegram Numbers**\n\n"
            "Здесь вы можете покупать и продавать красивые номера Telegram.\n"
            "Комиссия: 1%\n\n"
            "Функция в разработке...",
            parse_mode='Markdown'
        )
    elif query.data == "usernames":
        await query.edit_message_text(
            "👤 **Торговля Telegram Usernames**\n\n"
            "Здесь вы можете покупать и продавать уникальные юзернеймы.\n"
            "Комиссия: 1%\n\n"
            "Функция в разработке...",
            parse_mode='Markdown'
        )
    else:
        # Обработка других кнопок
        await query.edit_message_text(
            f"Вы выбрали: {query.data}\n\nФункция в разработке..."
        )


async def setup_bot_menu(application):
    """Настройка меню бота и команд"""
    # Установка команд бота
    commands = [
        BotCommand("start", "Главное меню"),
        BotCommand("marketplace", "Открыть NFT маркетплейс"),
        BotCommand("help", "Справка по боту"),
    ]
    
    await application.bot.set_my_commands(commands)
    
    # Установка кнопки меню как Web App
    menu_button = MenuButtonWebApp(
        text="🎁 Маркетплейс",
        web_app=WebAppInfo(url=WEBAPP_URL)
    )
    
    await application.bot.set_chat_menu_button(menu_button=menu_button)
    print("✅ Меню бота настроено")


def main() -> None:
    """Главная функция - точка входа приложения"""
    print("🚀 Запуск Telegram Marketplace Bot...")
    print(f"📱 Токен бота: {BOT_TOKEN}")
    
    # Запуск веб-сервера в отдельном потоке
    web_server_thread = threading.Thread(target=start_web_server, daemon=True)
    web_server_thread.start()
    
    print("✅ Веб-сервер запущен на порту 8000")
    print("🌐 Для работы Web App нужен HTTPS URL:")
    print("   1. Установите ngrok: https://ngrok.com/download")
    print("   2. Запустите: ngrok http 8000")
    print("   3. Скопируйте HTTPS URL и обновите код")
    print("   4. Или используйте временный URL: https://getgems.io/")
    print()
    
    # Создание приложения
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("marketplace", marketplace_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Настройка меню после инициализации
    application.job_queue.run_once(
        lambda context: setup_bot_menu(application), 
        when=1
    )
    
    print("🔄 Начинаю polling...")
    
    # Запуск бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()