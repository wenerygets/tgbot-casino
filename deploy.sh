#!/bin/bash
# Скрипт деплоя на Ubuntu сервер
# Запускать на сервере: bash deploy.sh

set -e

echo "🚀 Начинаем деплой..."

# 1. Обновление и установка Docker
apt-get update -y
apt-get install -y docker.io docker-compose curl

# 2. Создаём папку проекта
mkdir -p /opt/tgbot
cd /opt/tgbot

echo "✅ Docker установлен"

# 3. Запускаем
docker-compose down 2>/dev/null || true
docker-compose up -d --build

echo ""
echo "✅ Готово! Бот и веб-приложение запущены."
echo "🌐 Mini App доступен на: http://$(curl -s ifconfig.me)"
echo ""
echo "Команды управления:"
echo "  docker-compose logs -f     — логи"
echo "  docker-compose restart     — перезапуск"
echo "  docker-compose down        — остановка"
