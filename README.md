# Password Manager

Проект менеджера паролей предназначен для безопасного хранения и управления паролями, привязанных к именам сервисов.

## Требования

- Docker
- Docker Compose
- Git

## Установка и запуск

1. Клонируйте репозиторий:
git clone https://github.com/VasilijBirukow/PasswordManager.git

2. Перейдите в директорию проекта:

cd password_manager

3. Запустите сервисы с помощью Docker Compose:

docker-compose up --build


После запуска, API будет доступен по адресу `http://localhost:8000/`.

## API Endpoints

- `POST /password/{service_name}`: Создать или заменить пароль для указанного сервиса.
- `GET /password/{service_name}`: Получить пароль по имени сервиса.
- `GET /password/?service_name={part_of_service_name}`: Поиск паролей по части имени сервиса.
