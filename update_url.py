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