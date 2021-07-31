## Телеграм-бот, который присылает актуальный гороскоп.

### Если бота давно не запускали, ему может понадобиться минутка, чтобы проснуться.

Телеграм: `@realprophet_bot`

`conf.py, offline_bot.py` - используются для локального запуска бота.
Остальные файлы служат для flask приложения для запуска сервера на Heroku.

Обкачка происходит со страницы https://horo.mail.ru/

Используются следующие библиотеки: `telebot`, `flask`, `requests`, `bs4`


Пример работы:

`/start`

![image](https://user-images.githubusercontent.com/42929213/125284224-ddd3c000-e321-11eb-9dbc-ea1a084ff985.png
)

Выбор `Овен`

![image](https://user-images.githubusercontent.com/42929213/125284246-e5936480-e321-11eb-8850-429eaac4b244.png)

Выбор `Назад в меню`

![image](https://user-images.githubusercontent.com/42929213/125284263-e9bf8200-e321-11eb-8822-2601bf5edc35.png)
