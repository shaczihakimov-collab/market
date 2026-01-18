#!/usr/bin/env python3
"""
Быстрый деплой на GitHub Pages
"""

import os
import shutil

def create_github_pages():
    """Создает файлы для GitHub Pages"""
    
    # Создаем папку docs
    if os.path.exists('docs'):
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