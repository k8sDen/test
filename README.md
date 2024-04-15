### Структура проекта

    .
    ├── app                     # Бэкенд django 5
    ├── static                  # Статика
    ├── web                     # Фронтенд vue 3
    ├── docker-compose.yml      # Файл docker-compose
    ├── dump.sql                # Дамп базы данных PostgreSQL
    ├── nginx.conf              # Конфигурация nginx
    └── README.md

### Серверное ПО

| A          |       B |
|------------|--------:|
| Django     |   5.0.4 |
| Python     |  3.11.4 |
| Rabbitmq   |       3 |
| Redis      |   7.0.1 |
| PostgreSQL |    15.1 |
| Nginx      |  1.25.4 |
| Node.js    | 18.13.0 |
| Vue.js     |       3 |

# Как развернуть проект локально?

#### 1. Клонируем проект

```code
git clone git@github.com:k8sDen/test.git
```

#### 2. Копируем env.example и создаем .env

```code
cp app/.env.example app/.env
```

#### 3. Выполняем следующую команду

```code
docker-compose build
docker-compose up -d
```

#### Сайт доступен по адресу `http://127.0.0.1`

#### Админ панель

```code
логин: admin
пароль: admin
```

# Как устроен процесс импорта XLS файла.

#### 1. Файл импортируется из frontend проекта.

Так как у предоставленного файла формат `XLS`, в проекте используется движок `xlrd`. Если у вас файл `XLSX`, нужно будет поменять движок на `openpyxl`.