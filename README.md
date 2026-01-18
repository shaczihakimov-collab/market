[deploy_to_github.py](https://github.com/user-attachments/files/24696230/deploy_to_github.py)
#!/usr/bin/env python3
"""
Быстрый деплой на GitHub Pages
"""

import os
import shutil

def create_github_pages():
    """Создает файлы для GitHub Pages"""
    
    # Создаем папку docs
    if os.path.exists('docs'):[Uploading index.html…]()
[getgems_marketplace.html](https://github.com/user-attachments/files/24696232/getgems_marketplace.html)
[deploy_webapp.py](https://github.com/user-attachments/files/24696231/deploy_webapp.py)

        shutil.rmtree('docs')
    os.makedirs('docs')
    
    # Копируем файлы
    shutil.copy('getgems_marketplace.html', 'docs/index.html')
    
    # Создаем _config.yml
    with open('docs/_config.yml', 'w') as f:
        f.write('theme: jekyll-theme-minimal\n')
    
    print("✅ Файлы созданы в папке 'docs'")
    print("\n📋 Инструкция:")
    print("1. Создайте репозиторий на GitHub")
    print("2. Загрузите все файлы")
    print("3. В Settings > Pages выберите 'Deploy from a branch'")
    print("4. Выберите 'main' и '/docs'")
    print("5. Получите URL: https://username.github.io/repo-name/")
    print("6. Обновите WEBAPP_URL в main.py")

if __name__ == "__main__":
    create_github_pages()
#!/usr/bin/env python3
"""
Деплой webapp.html на бесплатный хостинг
"""

import os
import shutil
import webbrowser

def create_github_pages_setup():
    """Создает файлы для GitHub Pages"""
    
    # Создаем папку для GitHub Pages
    if not os.path.exists('docs'):
        os.makedirs('docs')
    
    # Копируем webapp.html как index.html
    shutil.copy('webapp.html', 'docs/index.html')
    
    # Создаем _config.yml для GitHub Pages
    with open('docs/_config.yml', 'w') as f:
        f.write('theme: jekyll-theme-minimal\n')
    
    print("✅ Файлы для GitHub Pages созданы в папке 'docs'")
    print("\n📋 Инструкция для GitHub Pages:")
    print("1. Создайте репозиторий на GitHub")
    print("2. Загрузите все файлы")
    print("3. В Settings > Pages выберите 'Deploy from a branch'")
    print("4. Выберите 'main' и '/docs'")
    print("5. Получите URL вида: https://username.github.io/repo-name/")
    print("6. Используйте этот URL в update_url.py")

def create_netlify_setup():
    """Создает файлы для Netlify"""
    
    # Создаем папку для Netlify
    if not os.path.exists('netlify'):
        os.makedirs('netlify')
    
    # Копируем webapp.html как index.html
    shutil.copy('webapp.html', 'netlify/index.html')
    
    # Создаем _redirects для SPA
    with open('netlify/_redirects', 'w') as f:
        f.write('/*    /index.html   200\n')
    
    print("✅ Файлы для Netlify созданы в папке 'netlify'")
    print("\n📋 Инструкция для Netlify:")
    print("1. Перейдите на netlify.com")
    print("2. Перетащите папку 'netlify' на сайт")
    print("3. Получите URL вида: https://random-name.netlify.app/")
    print("4. Используйте этот URL в update_url.py")

def main():
    print("🚀 Деплой кастомного маркетплейса")
    print("=" * 40)
    
    print("\nВыберите способ деплоя:")
    print("1. GitHub Pages (бесплатно)")
    print("2. Netlify (бесплатно)")
    print("3. Оба варианта")
    
    choice = input("\nВведите номер (1-3): ").strip()
    
    if choice == "1":
        create_github_pages_setup()
    elif choice == "2":
        create_netlify_setup()
    elif choice == "3":
        create_github_pages_setup()
        create_netlify_setup()
    else:
        print("❌ Неверный выбор")
        return
    
    print("\n🔗 Быстрые ссылки:")
    print("GitHub: https://github.com/new")
    print("Netlify: https://app.netlify.com/drop")

if __name__ == "__main__":
    main()
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <meta http-equiv="ngrok-skip-browser-warning" content="true">
    <title>Getgems: купить и продать подарки</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0f0f0f;
            color: #ffffff;
            overflow-x: hidden;
            min-height: 100vh;
        }

        .header {
            position: sticky;
            top: 0;
            background: #0f0f0f;
            border-bottom: 1px solid #2a2a2a;
            padding: 12px 16px;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 18px;
            font-weight: 600;
            color: #ffffff;
        }

        .logo::after {
            content: "✓";
            background: #0088cc;
            color: white;
            border-radius: 50%;
            width: 16px;
            height: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: bold;
        }

        .header-actions {
            display: flex;
            gap: 12px;
        }

        .header-btn {
            background: none;
            border: none;
            color: #888;
            font-size: 18px;
            cursor: pointer;
            padding: 4px;
        }

        .tabs {
            display: flex;
            padding: 0 16px;
            background: #0f0f0f;
            border-bottom: 1px solid #2a2a2a;
            overflow-x: auto;
        }

        .tab {
            padding: 16px 0;
            margin-right: 32px;
            color: #888;
            cursor: pointer;
            border-bottom: 2px solid transparent;
            white-space: nowrap;
            font-size: 15px;
            transition: all 0.2s;
        }

        .tab.active {
            color: #ffffff;
            border-bottom-color: #ffffff;
        }

        .search-section {
            padding: 16px;
            background: #0f0f0f;
        }

        .search-bar {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 8px;
            padding: 12px 16px;
            color: #ffffff;
            width: 100%;
            margin-bottom: 16px;
            font-size: 16px;
        }

        .search-bar::placeholder {
            color: #666;
        }

        .search-bar:focus {
            outline: none;
            border-color: #0088cc;
        }

        .toolbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
        }

        .filters {
            display: flex;
            gap: 8px;
            overflow-x: auto;
        }

        .filter-btn {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 6px;
            padding: 6px 12px;
            color: #ffffff;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
            font-size: 14px;
            transition: all 0.2s;
        }

        .filter-btn:hover {
            background: #2a2a2a;
        }

        .filter-btn.active {
            background: #0088cc;
            border-color: #0088cc;
        }

        .filter-btn::after {
            content: "▼";
            font-size: 10px;
            opacity: 0.7;
        }

        .view-controls {
            display: flex;
            gap: 8px;
        }

        .view-btn {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 6px;
            padding: 8px;
            color: #888;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.2s;
        }

        .view-btn.active {
            color: #ffffff;
            background: #2a2a2a;
        }

        .nft-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            padding: 16px;
            padding-bottom: 100px;
        }

        .nft-card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 12px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.3s ease;
            position: relative;
        }

        .nft-card:hover {
            transform: translateY(-2px);
            border-color: #0088cc;
            box-shadow: 0 8px 25px rgba(0, 136, 204, 0.2);
        }

        .nft-image {
            position: relative;
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            overflow: hidden;
        }

        .nft-image.blue { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .nft-image.green { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
        .nft-image.purple { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .nft-image.pink { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .nft-image.orange { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
        .nft-image.gray { background: linear-gradient(135deg, #636363 0%, #a2ab58 100%); }
        .nft-image.red { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
        .nft-image.cyan { background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); }

        .add-btn {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(0,0,0,0.7);
            border: none;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            color: white;
            cursor: pointer;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s;
        }

        .add-btn:hover {
            background: #0088cc;
            transform: scale(1.1);
        }

        .offchain-badge {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(0,0,0,0.8);
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 10px;
            display: flex;
            align-items: center;
            gap: 4px;
            color: #ffd700;
            font-weight: 500;
        }

        .offchain-badge::before {
            content: "⚡";
            font-size: 10px;
        }

        .nft-info {
            padding: 12px;
        }

        .nft-actions {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }

        .action-btn {
            background: none;
            border: none;
            color: #666;
            cursor: pointer;
            font-size: 18px;
            transition: all 0.2s;
            padding: 4px;
        }

        .action-btn:hover {
            color: #0088cc;
            transform: scale(1.2);
        }

        .nft-title {
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 6px;
            color: #ffffff;
            line-height: 1.3;
        }

        .nft-price {
            display: flex;
            align-items: center;
            gap: 6px;
            color: #0088cc;
            font-weight: 700;
            font-size: 16px;
        }

        .nft-price::before {
            content: "💎";
            font-size: 14px;
        }

        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #0f0f0f;
            border-top: 1px solid #2a2a2a;
            display: flex;
            justify-content: space-around;
            padding: 8px 0 12px;
            z-index: 100;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #666;
            text-decoration: none;
            font-size: 11px;
            cursor: pointer;
            transition: all 0.2s;
            padding: 4px 8px;
            border-radius: 8px;
            min-width: 60px;
        }

        .nav-item.active {
            color: #0088cc;
        }

        .nav-icon {
            font-size: 20px;
            margin-bottom: 2px;
        }

        .bot-info {
            position: fixed;
            bottom: 70px;
            left: 50%;
            transform: translateX(-50%);
            color: #666;
            font-size: 12px;
            z-index: 50;
        }

        .notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #0088cc;
            color: white;
            padding: 12px 16px;
            border-radius: 8px;
            z-index: 1000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            font-size: 14px;
        }

        .notification.show {
            transform: translateX(0);
        }

        /* Анимации */
        .pulse {
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.7; }
            100% { opacity: 1; }
        }

        .loading {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 200px;
            font-size: 16px;
            color: #666;
        }

        /* Скроллбар */
        ::-webkit-scrollbar {
            width: 4px;
            height: 4px;
        }

        ::-webkit-scrollbar-track {
            background: #1a1a1a;
        }

        ::-webkit-scrollbar-thumb {
            background: #666;
            border-radius: 2px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #888;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">Getgems</div>
        <div class="header-actions">
            <button class="header-btn">⋯</button>
            <button class="header-btn">✕</button>
        </div>
    </div>

    <div class="tabs">
        <div class="tab active" data-tab="collection">Коллекция</div>
        <div class="tab" data-tab="history">История</div>
        <div class="tab" data-tab="stats">Статистика</div>
        <div class="tab" data-tab="offers">Предложения</div>
        <div class="tab" data-tab="comments">Комментарии</div>
    </div>

    <div class="search-section">
        <input type="text" class="search-bar" placeholder="Название или описание" id="searchInput">
        
        <div class="toolbar">
            <div class="filters">
                <button class="filter-btn active" data-filter="all">🔧 Коллекции</button>
                <button class="filter-btn" data-filter="backdrop">Backdrop</button>
                <button class="filter-btn" data-filter="symbol">Symbol</button>
                <button class="filter-btn" data-filter="model">Model</button>
            </div>
            
            <div class="view-controls">
                <button class="view-btn">↕️</button>
                <button class="view-btn">📷</button>
                <button class="view-btn active">☰</button>
            </div>
        </div>
    </div>

    <div class="nft-grid" id="nftGrid">
        <!-- NFT карточки будут добавлены через JavaScript -->
    </div>

    <div class="bottom-nav">
        <a href="#" class="nav-item active">
            <div class="nav-icon">🏪</div>
            <div>Маркет</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">⭐</div>
            <div>Звёзды</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">📋</div>
            <div>Каталог</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">🛒</div>
            <div>Корзина</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">👤</div>
            <div>Профиль</div>
        </a>
    </div>

    <div class="bot-info">@GetgemsNftBot</div>
    <div class="notification" id="notification"></div>

    <script>
    <script>
        // Обход предупреждения ngrok
        if (window.location.href.includes('ngrok-free.dev') && !window.location.href.includes('ngrok-skip-browser-warning')) {
            window.location.href = window.location.href + (window.location.href.includes('?') ? '&' : '?') + 'ngrok-skip-browser-warning=true';
        }
        
        // Инициализация Telegram Web App
        let tg;
        try {
            tg = window.Telegram.WebApp;
            tg.ready();
            tg.expand();
            tg.setHeaderColor('#0f0f0f');
            tg.setBackgroundColor('#0f0f0f');
        } catch (e) {
            console.log('Telegram Web App не доступен');
        }

        // Данные NFT (точно как на скриншоте)
        const nftData = [
            { id: 1, name: "Diamond Ring #888", price: 888, emoji: "📱", color: "blue", offchain: true, rarity: "legendary" },
            { id: 2, name: "Durov's Cap #3082", price: 749, emoji: "🧢", color: "green", offchain: false, rarity: "epic" },
            { id: 3, name: "Witch Hat #39692", price: 25, emoji: "🎩", color: "purple", offchain: true, rarity: "common" },
            { id: 4, name: "Clover Pin #100057", price: 777, emoji: "🍭", color: "pink", offchain: false, rarity: "legendary" },
            { id: 5, name: "Scared Cat #17205", price: 120, emoji: "🐱", color: "orange", offchain: true, rarity: "rare" },
            { id: 6, name: "Hex Pot #39470", price: 60, emoji: "🧪", color: "gray", offchain: true, rarity: "uncommon" },
            { id: 7, name: "Magic Mushroom #2156", price: 340, emoji: "🍄", color: "red", offchain: false, rarity: "rare" },
            { id: 8, name: "Pixel Monster #8901", price: 199, emoji: "👾", color: "cyan", offchain: false, rarity: "rare" }
        ];

        let cart = [];
        let favorites = [];

        // Функция показа уведомлений
        function showNotification(message) {
            const notification = document.getElementById('notification');
            notification.textContent = message;
            notification.classList.add('show');
            
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        }

        // Функция создания NFT карточки
        function createNFTCard(nft) {
            return `
                <div class="nft-card" data-id="${nft.id}" data-rarity="${nft.rarity}" data-offchain="${nft.offchain}">
                    <div class="nft-image ${nft.color}">
                        ${nft.emoji}
                        <button class="add-btn" onclick="addToCart(${nft.id})">+</button>
                        ${nft.offchain ? '<div class="offchain-badge">offchain</div>' : ''}
                    </div>
                    <div class="nft-info">
                        <div class="nft-actions">
                            <button class="action-btn" onclick="toggleLike(this, ${nft.id})">♡</button>
                            <button class="action-btn" onclick="showOptions(${nft.id})">⋯</button>
                        </div>
                        <div class="nft-title">${nft.name}</div>
                        <div class="nft-price">${nft.price}</div>
                    </div>
                </div>
            `;
        }

        // Функция отображения NFT
        function renderNFTs(filter = 'all') {
            const grid = document.getElementById('nftGrid');
            let filteredNFTs = nftData;

            if (filter === 'backdrop') {
                filteredNFTs = nftData.filter(nft => nft.rarity === 'legendary' || nft.rarity === 'epic');
            } else if (filter === 'symbol') {
                filteredNFTs = nftData.filter(nft => nft.offchain);
            } else if (filter === 'model') {
                filteredNFTs = nftData.filter(nft => nft.price > 200);
            }

            grid.innerHTML = filteredNFTs.map(createNFTCard).join('');
        }

        // Функция добавления в корзину
        function addToCart(nftId) {
            const nft = nftData.find(n => n.id === nftId);
            cart.push(nft);
            showNotification(`${nft.name} добавлен в корзину! (${cart.length})`);
            
            // Отправляем данные в Telegram
            if (tg && tg.sendData) {
                tg.sendData(JSON.stringify({
                    action: 'add_to_cart',
                    nft: nft,
                    cart_count: cart.length
                }));
            }
        }

        // Функция лайка
        function toggleLike(button, nftId) {
            const nft = nftData.find(n => n.id === nftId);
            
            if (button.textContent === '♡') {
                button.textContent = '♥';
                button.style.color = '#ff4757';
                favorites.push(nftId);
                showNotification(`${nft.name} добавлен в избранное!`);
            } else {
                button.textContent = '♡';
                button.style.color = '#666';
                favorites = favorites.filter(id => id !== nftId);
                showNotification(`${nft.name} удален из избранного`);
            }
        }

        // Функция показа опций
        function showOptions(nftId) {
            const nft = nftData.find(n => n.id === nftId);
            showNotification(`Опции для ${nft.name}`);
        }

        // Обработчики событий
        document.addEventListener('DOMContentLoaded', function() {
            renderNFTs();

            // Фильтры
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.addEventListener('click', function() {
                    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    
                    const filter = this.dataset.filter;
                    renderNFTs(filter);
                });
            });

            // Поиск
            document.getElementById('searchInput').addEventListener('input', function(e) {
                const query = e.target.value.toLowerCase();
                const cards = document.querySelectorAll('.nft-card');
                
                cards.forEach(card => {
                    const title = card.querySelector('.nft-title').textContent.toLowerCase();
                    if (title.includes(query)) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });

            // Клики по NFT
            document.addEventListener('click', function(e) {
                const card = e.target.closest('.nft-card');
                if (card && !e.target.closest('.add-btn') && !e.target.closest('.action-btn')) {
                    const nftId = parseInt(card.dataset.id);
                    const nft = nftData.find(n => n.id === nftId);
                    
                    showNotification(`Просмотр ${nft.name} - ${nft.price} 💎`);
                    
                    // Отправляем данные в Telegram
                    if (tg && tg.sendData) {
                        tg.sendData(JSON.stringify({
                            action: 'view_nft',
                            nft: nft
                        }));
                    }
                }
            });

            // Табы
            document.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', function() {
                    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                    this.classList.add('active');
                    
                    const tabName = this.dataset.tab;
                    showNotification(`Переход в раздел: ${this.textContent}`);
                });
            });

            // Навигация
            document.querySelectorAll('.nav-item').forEach(item => {
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
                    this.classList.add('active');
                    
                    const section = this.querySelector('div:last-child').textContent;
                    showNotification(`Переход в: ${section}`);
                });
            });
        });

        // Настройка главной кнопки Telegram
        if (tg && tg.MainButton) {
            tg.MainButton.text = `Корзина (${cart.length})`;
            tg.MainButton.show();
            tg.MainButton.onClick(function() {
                if (tg.sendData) {
                    tg.sendData(JSON.stringify({
                        action: 'go_to_cart',
                        cart: cart,
                        total: cart.reduce((sum, item) => sum + item.price, 0)
                    }));
                }
            });
        }

        // Обработка закрытия приложения
        if (tg && tg.onEvent) {
            tg.onEvent('backButtonClicked', function() {
                tg.close();
            });
        }

        // Обновление счетчика корзины
        function updateCartButton() {
            if (tg && tg.MainButton) {
                tg.MainButton.text = `Корзина (${cart.length})`;
            }
        }

        // Переопределяем addToCart для обновления кнопки
        const originalAddToCart = addToCart;
        addToCart = function(nftId) {
            originalAddToCart(nftId);
            updateCartButton();
        };
    </script>
</body>
</html>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Getgems Marketplace</title>
    <style>
        body {
            background: #0f0f0f;
            color: white;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .loader {
            text-align: center;
        }
        .spinner {
            border: 3px solid #333;
            border-top: 3px solid #0088cc;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 20px;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="loader">
        <div class="spinner"></div>
        <p>Загрузка маркетплейса...</p>
    </div>
    
    <script>
        // Немедленное перенаправление на маркетплейс с обходом ngrok
        setTimeout(() => {
            const currentUrl = window.location.href;
            const baseUrl = currentUrl.split('?')[0];
            window.location.href = baseUrl + '/marketplace?ngrok-skip-browser-warning=true';
        }, 500);
    </script>
</body>
</html>
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
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Getgems</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #1a1a1a;
            color: white;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            overflow-x: hidden;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 16px 20px;
            border-bottom: 1px solid #333;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 18px;
            font-weight: 600;
        }

        .logo::after {
            content: "✓";
            background: #0088cc;
            color: white;
            border-radius: 50%;
            width: 16px;
            height: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
        }

        .header-actions {
            display: flex;
            gap: 12px;
        }

        .header-btn {
            background: none;
            border: none;
            color: #888;
            font-size: 18px;
            cursor: pointer;
        }

        .tabs {
            display: flex;
            padding: 0 20px;
            border-bottom: 1px solid #333;
        }

        .tab {
            padding: 16px 0;
            margin-right: 32px;
            color: #888;
            cursor: pointer;
            border-bottom: 2px solid transparent;
        }

        .tab.active {
            color: white;
            border-bottom-color: white;
        }

        .search-section {
            padding: 20px;
        }

        .search-bar {
            background: #2a2a2a;
            border: none;
            border-radius: 8px;
            padding: 12px 16px;
            color: white;
            width: 100%;
            margin-bottom: 20px;
        }

        .search-bar::placeholder {
            color: #666;
        }

        .filters {
            display: flex;
            gap: 12px;
            margin-bottom: 20px;
        }

        .filter-btn {
            background: #2a2a2a;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            color: white;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .filter-btn::after {
            content: "▼";
            font-size: 10px;
        }

        .nft-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
            gap: 16px;
            padding: 0 20px 100px;
        }

        .nft-card {
            background: #2a2a2a;
            border-radius: 12px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
        }

        .nft-card:hover {
            transform: translateY(-2px);
        }

        .nft-image {
            position: relative;
            aspect-ratio: 1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
        }

        .nft-image.blue { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
        .nft-image.green { background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); }
        .nft-image.purple { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .nft-image.pink { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
        .nft-image.orange { background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%); }
        .nft-image.gray { background: linear-gradient(135deg, #636363 0%, #a2ab58 100%); }

        .add-btn {
            position: absolute;
            top: 8px;
            left: 8px;
            background: rgba(0,0,0,0.5);
            border: none;
            border-radius: 50%;
            width: 24px;
            height: 24px;
            color: white;
            cursor: pointer;
            font-size: 14px;
        }

        .offchain-badge {
            position: absolute;
            bottom: 8px;
            left: 8px;
            background: rgba(0,0,0,0.7);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .offchain-badge::before {
            content: "⚡";
            font-size: 8px;
        }

        .nft-info {
            padding: 12px;
        }

        .nft-actions {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }

        .action-btn {
            background: none;
            border: none;
            color: #666;
            cursor: pointer;
            font-size: 16px;
        }

        .nft-title {
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 4px;
        }

        .nft-price {
            display: flex;
            align-items: center;
            gap: 4px;
            color: #0088cc;
            font-weight: 600;
        }

        .nft-price::before {
            content: "💎";
            font-size: 12px;
        }

        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #1a1a1a;
            border-top: 1px solid #333;
            display: flex;
            justify-content: space-around;
            padding: 12px 0;
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
            color: #666;
            text-decoration: none;
            font-size: 12px;
        }

        .nav-item.active {
            color: white;
        }

        .nav-icon {
            font-size: 20px;
        }

        .bot-info {
            position: fixed;
            bottom: 70px;
            left: 50%;
            transform: translateX(-50%);
            color: #666;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="logo">Getgems</div>
        <div class="header-actions">
            <button class="header-btn">⋯</button>
            <button class="header-btn">✕</button>
        </div>
    </div>

    <div class="tabs">
        <div class="tab active">Коллекция</div>
        <div class="tab">История</div>
        <div class="tab">Статистика</div>
        <div class="tab">Предложения</div>
        <div class="tab">Комментарии</div>
    </div>

    <div class="search-section">
        <input type="text" class="search-bar" placeholder="Название или описание">
        
        <div class="filters">
            <button class="filter-btn">🔧 Коллекции</button>
            <button class="filter-btn">Backdrop</button>
            <button class="filter-btn">Symbol</button>
            <button class="filter-btn">Model</button>
        </div>
    </div>

    <div class="nft-grid">
        <div class="nft-card">
            <div class="nft-image blue">
                📱
                <button class="add-btn">+</button>
                <div class="offchain-badge">offchain</div>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Diamond Ring #888</div>
                <div class="nft-price">888</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image green">
                🧢
                <button class="add-btn">+</button>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Durov's Cap #3082</div>
                <div class="nft-price">749</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image purple">
                🎩
                <button class="add-btn">+</button>
                <div class="offchain-badge">offchain</div>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Witch Hat #39692</div>
                <div class="nft-price">25</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image pink">
                🍭
                <button class="add-btn">+</button>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Clover Pin #100057</div>
                <div class="nft-price">777</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image orange">
                🐱
                <button class="add-btn">+</button>
                <div class="offchain-badge">offchain</div>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Scared Cat #17205</div>
                <div class="nft-price">120</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image gray">
                🧪
                <button class="add-btn">+</button>
                <div class="offchain-badge">offchain</div>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Hex Pot #39470</div>
                <div class="nft-price">60</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image pink">
                🍄
                <button class="add-btn">+</button>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Magic Mushroom #2156</div>
                <div class="nft-price">340</div>
            </div>
        </div>

        <div class="nft-card">
            <div class="nft-image purple">
                👾
                <button class="add-btn">+</button>
            </div>
            <div class="nft-info">
                <div class="nft-actions">
                    <button class="action-btn">♡</button>
                    <button class="action-btn">⋯</button>
                </div>
                <div class="nft-title">Pixel Monster #8901</div>
                <div class="nft-price">199</div>
            </div>
        </div>
    </div>

    <div class="bottom-nav">
        <a href="#" class="nav-item active">
            <div class="nav-icon">🏪</div>
            <div>Маркет</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">⭐</div>
            <div>Звёзды</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">📋</div>
            <div>Каталог</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">🛒</div>
            <div>Корзина</div>
        </a>
        <a href="#" class="nav-item">
            <div class="nav-icon">👤</div>
            <div>Профиль</div>
        </a>
    </div>

    <div class="bot-info">@GetgemsNftBot</div>

    <script>
        // Добавляем интерактивность
        document.querySelectorAll('.nft-card').forEach(card => {
            card.addEventListener('click', () => {
                alert('NFT выбран! Функция покупки в разработке.');
            });
        });

        document.querySelectorAll('.action-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                if (btn.textContent === '♡') {
                    btn.textContent = '♥';
                    btn.style.color = '#ff4757';
                    setTimeout(() => {
                        btn.textContent = '♡';
                        btn.style.color = '#666';
                    }, 1000);
                }
            });
        });

        document.querySelectorAll('.add-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                alert('NFT добавлен в корзину!');
            });
        });
    </script>
</body>
</html>
#!/usr/bin/env python3
"""
Быстрая настройка кастомного маркетплейса
"""

import re
import subprocess
import sys

def update_webapp_url_in_code(new_url):
    """Обновляет WEBAPP_URL в main.py"""
    
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Заменяем WEBAPP_URL
    pattern = r'WEBAPP_URL = "[^"]*"'
    replacement = f'WEBAPP_URL = "{new_url}"'
    
    new_content = re.sub(pattern, replacement, content)
    
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ WEBAPP_URL обновлен на: {new_url}")

def main():
    print("🚀 Быстрая настройка кастомного маркетплейса")
    print("=" * 50)
    
    print("\n📋 У вас есть 3 варианта:")
    print("1. Использовать ngrok (рекомендуется)")
    print("2. Использовать бесплатный хостинг")
    print("3. Ввести готовый HTTPS URL")
    
    choice = input("\nВыберите вариант (1-3): ").strip()
    
    if choice == "1":
        print("\n🔧 Настройка ngrok:")
        print("1. Запустите в новом терминале: ngrok http 8000")
        print("2. Скопируйте HTTPS URL (например: https://abc123.ngrok.io)")
        
        url = input("\n🌐 Введите HTTPS URL от ngrok: ").strip()
        if url and url.startswith('https://'):
            if not url.endswith('/marketplace'):
                url += '/marketplace'
            update_webapp_url_in_code(url)
            print("\n✅ Готово! Теперь запустите: python main.py")
        else:
            print("❌ URL должен начинаться с https://")
    
    elif choice == "2":
        print("\n🌐 Настройка бесплатного хостинга:")
        subprocess.run([sys.executable, 'deploy_webapp.py'])
        
        url = input("\n🔗 Введите полученный HTTPS URL: ").strip()
        if url and url.startswith('https://'):
            update_webapp_url_in_code(url)
            print("\n✅ Готово! Теперь запустите: python main.py")
        else:
            print("❌ URL должен начинаться с https://")
    
    elif choice == "3":
        url = input("\n🔗 Введите HTTPS URL: ").strip()
        if url and url.startswith('https://'):
            update_webapp_url_in_code(url)
            print("\n✅ Готово! Теперь запустите: python main.py")
        else:
            print("❌ URL должен начинаться с https://")
    
    else:
        print("❌ Неверный выбор")

if __name__ == "__main__":
    main()
# Telegram Marketplace Bot - Getgems

Telegram бот с полноценным веб-приложением маркетплейса NFT.

## Функциональность

- Приветственное сообщение с информацией о маркетплейсе
- **Кнопка меню "🎁 Маркетплейс"** - быстрый доступ к Web App
- Команды бота: /start, /marketplace, /help
- Полноценное веб-приложение маркетплейса с фейковыми NFT
- Интерактивный интерфейс с коллекцией, поиском и фильтрами
- Интеграция с Telegram Web App API

## Файлы проекта

- `main.py` - Основной файл бота с встроенным веб-сервером
- `marketplace.html` - Веб-приложение маркетплейса
- `server.py` - Отдельный HTTP сервер (опционально)
- `requirements.txt` - Зависимости Python

## Установка и запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите бота:
```bash
python main.py
```

⚠️ **Важно**: Telegram Web Apps требуют HTTPS URL. Для локальной разработки:

### Вариант 1: Использовать ngrok (рекомендуется)
1. Установите ngrok: https://ngrok.com/download
2. Запустите: `ngrok http 8000`
3. Обновите URL в main.py на полученный HTTPS адрес

### Вариант 2: Бесплатные хостинги
- GitHub Pages
- Netlify 
- Vercel

Подробные инструкции в файле `setup_ngrok.md`

## Текущее состояние

Сейчас бот использует https://getgems.io/ для демонстрации.
Для вашего кастомного маркетплейса нужно настроить HTTPS хостинг.

## Альтернативный запуск

Можно запустить только веб-сервер:
```bash
python server.py
```

## Особенности

- При нажатии на "Торговать Telegram Gifts" сразу открывается мини-приложение
- Веб-приложение имитирует интерфейс Getgems с фейковыми NFT
- Интерактивные элементы: лайки, добавление в корзину, клики по NFT

## Требования

- Python 3.7+
- python-telegram-bot 20.7

## Токен бота

Токен: `8535517286:AAECqvGpe9fdRfori0SL98g3MK7jnfVvu6o`
python-telegram-bot==20.7
requests
#!/usr/bin/env python3
"""
Простой HTTP сервер для маркетплейса
"""

import http.server
import socketserver
import threading
import os

class MarketplaceHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/marketplace':
            self.path = '/marketplace.html'
        return super().do_GET()

def start_server(port=8000):
    """Запуск HTTP сервера"""
    handler = MarketplaceHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🌐 HTTP сервер запущен на http://localhost:{port}")
        print(f"📱 Маркетплейс доступен по адресу: http://localhost:{port}/marketplace")
        httpd.serve_forever()

if __name__ == "__main__":
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    print("Нажмите Ctrl+C для остановки сервера")
    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("\n🛑 Сервер остановлен")
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
#!/usr/bin/env python3
"""
Автоматическая настройка ngrok
"""

import subprocess
import sys
import time
import re
import requests
import json

NGROK_TOKEN = "38Qrn2KYpxvExElI9QI8SrBLhiN_2iHqGg9PBJU6cbmuizs1v"

def setup_ngrok():
    """Настройка ngrok с токеном"""
    try:
        # Настройка токена
        result = subprocess.run(['ngrok', 'config', 'add-authtoken', NGROK_TOKEN], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Токен ngrok настроен успешно")
            return True
        else:
            print(f"❌ Ошибка настройки токена: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ ngrok не найден. Скачайте с https://ngrok.com/download")
        return False

def get_ngrok_url():
    """Получение URL из ngrok API"""
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        if response.status_code == 200:
            tunnels = response.json()['tunnels']
            for tunnel in tunnels:
                if tunnel['config']['addr'] == 'http://localhost:8000':
                    return tunnel['public_url']
        return None
    except:
        return None

def update_bot_url(url):
    """Обновление URL в main.py"""
    try:
        with open('main.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Заменяем URL
        pattern = r'web_app=WebAppInfo\(url="[^"]+"\)'
        replacement = f'web_app=WebAppInfo(url="{url}/marketplace")'
        new_content = re.sub(pattern, replacement, content)
        
        with open('main.py', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ URL обновлен: {url}/marketplace")
        return True
    except Exception as e:
        print(f"❌ Ошибка обновления URL: {e}")
        return False

def main():
    print("🚀 Автоматическая настройка ngrok для Telegram Web App")
    print("=" * 50)
    
    # Настройка токена
    if not setup_ngrok():
        return
    
    print("\n📋 Инструкции:")
    print("1. Запустите бота: python main.py")
    print("2. В новом терминале запустите: ngrok http 8000")
    print("3. Запустите этот скрипт еще раз для получения URL")
    print("\nИли запустите все автоматически:")
    print("python setup_ngrok_auto.py --auto")
    
    if len(sys.argv) > 1 and sys.argv[1] == '--auto':
        print("\n🔄 Автоматический запуск...")
        
        # Запуск ngrok в фоне
        try:
            subprocess.Popen(['ngrok', 'http', '8000'], 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
            print("✅ ngrok запущен")
            
            # Ждем запуска ngrok
            print("⏳ Ожидание запуска ngrok...")
            time.sleep(5)
            
            # Получаем URL
            url = get_ngrok_url()
            if url:
                if url.startswith('http://'):
                    url = url.replace('http://', 'https://')
                
                print(f"🌐 Получен URL: {url}")
                
                # Обновляем бота
                if update_bot_url(url):
                    print("\n✅ Настройка завершена!")
                    print("🔄 Теперь запустите бота: python main.py")
                else:
                    print("❌ Не удалось обновить URL")
            else:
                print("❌ Не удалось получить URL от ngrok")
                
        except Exception as e:
            print(f"❌ Ошибка автоматического запуска: {e}")

if __name__ == "__main__":
    main()
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
#!/usr/bin/env python3
"""
Скрипт для обновления URL в main.py
"""

import re

def update_webapp_url(new_url):
    """Обновляет URL веб-приложения в main.py"""
    
    # Читаем файл
    with open('main.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Находим и заменяем все URL
    patterns = [
        r'web_app=WebAppInfo\(url="[^"]+"\)',
        r'WebAppInfo\(url="[^"]+"\)'
    ]
    
    for pattern in patterns:
        replacement = f'WebAppInfo(url="{new_url}")'
        content = re.sub(pattern, replacement, content)
    
    # Записываем обратно
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Все URL обновлены на: {new_url}")
    print("🔄 Перезапустите бота для применения изменений")

if __name__ == "__main__":
    print("🔧 Обновление URL веб-приложения")
    print()
    print("Примеры URL:")
    print("  https://abc123.ngrok.io/marketplace")
    print("  https://getgems.io/")
    print()
    
    new_url = input("Введите новый HTTPS URL: ").strip()
    
    if new_url.startswith('https://'):
        update_webapp_url(new_url)
    else:
        print("❌ URL должен начинаться с https://")
# Инструкция по загрузке в GitHub

## Способ 1: Через веб-интерфейс GitHub
1. Откройте https://github.com/shaczihakimov-collab/market
2. Нажмите "uploading an existing file"
3. Перетащите все файлы из папки проекта
4. Напишите commit message: "Add marketplace bot files"
5. Нажмите "Commit changes"

## Способ 2: Через Git командную строку
```bash
git clone https://github.com/shaczihakimov-collab/market.git
cd market
# Скопируйте все файлы в эту папку
git add .
git commit -m "Add marketplace bot files"
git push origin main
```

## Настройка GitHub Pages
1. Перейдите в Settings > Pages
2. Source: "Deploy from a branch"
3. Branch: "main"
4. Folder: "/docs"
5. Нажмите "Save"

## Ваш URL после деплоя
https://shaczihakimov-collab.github.io/market/

Обычно деплой занимает 2-5 минут.

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Перенаправление...</title>
    <script>
        // Автоматическое перенаправление с обходом предупреждения ngrok
        window.location.href = window.location.href + '?ngrok-skip-browser-warning=true';
    </script>
</head>
<body>
    <p>Перенаправление на маркетплейс...</p>
</body>
</html>
#!/usr/bin/env python3
"""
Проверка статуса GitHub Pages
"""

import requests
import time

def check_github_pages():
    url = "https://shaczihakimov-collab.github.io/market/"
    
    print(f"🔍 Проверяю доступность: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ GitHub Pages работает!")
            print(f"📄 Размер страницы: {len(response.text)} символов")
            
            # Проверяем, что это наша страница
            if "Getgems" in response.text:
                print("✅ Маркетплейс загружен корректно!")
                return True
            else:
                print("⚠️ Страница загружена, но содержимое не соответствует ожидаемому")
                return False
                
        elif response.status_code == 404:
            print("❌ 404 - GitHub Pages еще не настроен или файлы не загружены")
            print("\n📋 Что нужно сделать:")
            print("1. Загрузите все файлы в репозиторий")
            print("2. Настройте GitHub Pages: Settings > Pages > Deploy from branch > main > /docs")
            print("3. Подождите 2-10 минут")
            return False
            
        else:
            print(f"❌ Ошибка {response.status_code}: {response.reason}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка подключения: {e}")
        return False

if __name__ == "__main__":
    check_github_pages()
