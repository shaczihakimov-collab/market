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