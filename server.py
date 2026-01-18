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