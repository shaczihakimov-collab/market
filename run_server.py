#!/usr/bin/env python3
"""
Запуск HTTP сервера для NFT маркетплейса
"""

import http.server
import socketserver
import webbrowser
import threading
import time

class NFTHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/rent':
            self.path = '/nft_rent_complete.html'
        elif self.path == '/getgems':
            self.path = '/getgems_new.html'
        elif self.path == '/marketplace':
            self.path = '/marketplace.html'
        return super().do_GET()

def start_server(port=8000):
    """Запуск HTTP сервера"""
    handler = NFTHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"🚀 Сервер запущен на http://localhost:{port}")
            print(f"🏠 Аренда NFT: http://localhost:{port}/rent")
            print(f"💎 Getgems: http://localhost:{port}/getgems")
            print(f"📱 Маркетплейс: http://localhost:{port}/marketplace")
            print("\nНажмите Ctrl+C для остановки")
            
            # Автоматически открываем браузер через 1 секунду
            def open_browser():
                time.sleep(1)
                webbrowser.open(f'http://localhost:{port}/rent')
            
            threading.Thread(target=open_browser, daemon=True).start()
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Сервер остановлен")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Порт {port} уже используется. Попробуйте другой порт.")
        else:
            print(f"❌ Ошибка запуска сервера: {e}")

if __name__ == "__main__":
    start_server()