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