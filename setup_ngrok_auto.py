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