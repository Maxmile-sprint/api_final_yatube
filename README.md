# api_final_yatube
## api final yatube - Многофункциональный API-сервис для взаимодествия с социальной сетью Yatube. 
### Как запустить проект:

#### Клонировать репозиторий и перейти в него в командной строке:

###### *git clone (git@github.com:Maxmile-sprint/api_final_yatube.git)*

###### *cd api_final_yatube*

#### Cоздать и активировать виртуальное окружение:

###### *python3 -m venv env*

###### *source env/bin/activate*

##### Установить зависимости из файла requirements.txt:

###### *python3 -m pip install --upgrade pip*

###### *pip install -r requirements.txt*

##### Выполнить миграции:

###### *python3 manage.py migrate*

##### Запустить проект:

###### *python3 manage.py runserver*

#### Примеры запросов для получения, создания и изменения постов и комментариев, а также для оформления подписок на авторов

###### */api/v1/posts/*
###### */api/v1/posts/{id}/*
###### *api/v1/posts/{post_id}/comments/*
###### *api/v1/posts/{post_id}/comments/{id}/*
###### *api/v1/groups/*
###### *api/v1/groups/{id}/*
###### *api/v1/follow/*
