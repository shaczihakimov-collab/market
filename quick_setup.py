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