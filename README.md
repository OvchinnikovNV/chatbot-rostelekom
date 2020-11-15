# Северо-Западный IT-хаб

## Команда MOЯZE

![logo](https://github.com/OvchinnikovNV/chatbot-rostelekom/blob/main/rsc/team.gif)

## Кейс

Создание чат-бота - интерактивного помощника по порталу rt.ru, позволяющий в режиме диалога предоставить необходимую для клиента информацию.

## Результаты 1-го чекпоинта

Директория backend: чат-бот на python, использующий нейронную сеть для определния категории вопроса пользователя.

![backend](https://github.com/OvchinnikovNV/chatbot-rostelekom/blob/main/rsc/backend.gif)

Директория frontend: реализована web-страница с виджетом чат-бота.

![frontend](https://github.com/OvchinnikovNV/chatbot-rostelekom/blob/main/rsc/frontend.gif)

Frontend и backend на данный момент не связаны.

## Результаты 2-го чекпоинта (финальный результат)

1) Связаны backend и frontend при помощи фреймворка Flask.

2) Теперь в ответе на вопрос чат-бот генерирует сообщение с ссылкой на необходимый раздел в https://moscow.rt.ru/support

3) Вручную добавлены данные в dataset для получения ссылок на необходимые подкатегории в разделе https://moscow.rt.ru/support

4) Добавлены уникальные ответы чат-бота для категорий/подкатегорий раздела https://moscow.rt.ru/support

![result]()

## Installation

Для того, чтобы запустить чат-бот, необходимо:

1) Скачать директорию chatbot-rostelekom

2) Установить все требующиеся библиотеки любым удобным способом и среду исполнения python

3) Перейти в директорию src/backend и запустить файл main.py

4) Перейти в директорию chatbot-rostelekom и запустить файл app.py

5) Открыть браузер и перейти по адресу localhost:5000
