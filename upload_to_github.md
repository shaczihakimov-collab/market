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