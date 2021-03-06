# Пульт охраны банка

Данный пункт охраны обладает следующими функциями:

1. Отслеживание посещений секретного хранилища с 
   выявлением подозрительно длительных визитов;
   
2. Вывод списка активных карт доступа;

3. Вывод информации по каждому из владельцев
активных карт доступа.
   
## Перед началом работы

Для запуска пульта охраны следуйте следующим инструкциям:

1. Скачайте файлы проекта.

2. Создайте виртуальное окружение.
Для этого следуйте следующим указаниям:

    2.1. Создайте новое виртуальное окружение, запустив 
   в терминале следующую команду:
   
    ```bash
    python3 -m venv название_виртуального_окружения/полный/путь/до/папки/виртуального/окружения
    ```

    2.2. Теперь необходимо активировать виртуальное окружение, 
   для этого выполните следующую команду:
   
    ```bash
    source /полный/путь/до/папки/виртуального/окружения/bin/activate
    ```
    При желании получить больше информации или 
    использовать другие средства для создания виртуального окружения,
    можете ознакомиться со следующими ресурсами:
    
   [Что такое виртуальное окружение](https://devman.org/qna/12/chto-takoe-virtualnoe/)
    
   [Виртуальное окружение](https://devman.org/encyclopedia/pip/pip_virtualenv/)
    
   [Requirements.txt](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

3. Необходимо загрузить в виртуальное окружение библиотеки 
   из файла `requirements.txt`. 
Для этого, уже активировав виртуальное окружение, 
   выполните следующую команду:

    ```bash
    pip install -r requirements.txt
    ```
4. Для корректной работы пульта охраны необходимо загрузить 
   информацию, требуемую для подключения базы данных.
   
   Для этого создайте файл `.env`, в котором необходимо разместить 
следующие переменные окружения:
   - `DB_URL` - информация о базе данных следующего вида:
     	`postgres://USER:PASSWORD@HOST:PORT/NAME`, где:
     * postgres - используемая система управления базами данных;
     * USER - имя пользователя базы данных;
     * PASSWORD - пароль для доступа к базе данных;
     * HOST - адрес, по которому находится база данных;
     * PORT - номер серверного порта, используемого базой данных;
     * NAME - имя базы данных.
    
        При необходимости ознакомиться с возможностью 
       подключения другой системы управления
       базами данных, ознакомьтесь с [Документацией](https://github.com/jacobian/dj-database-url). 

   - `SECRET_KEY` - секретный ключ проекта. Например: very_very_secret_key;
   - `DEBUG` - маркер для включения и отключения дебаг-режима.
     Для включения дебаг-режима передайте в эту переменную значение `True`.
     Для выключения дебаг-режима передайте в эту переменную значение `False`.
      
   - `ALLOWED_HOSTS=127.0.0.1,localhost` - список доменов, для которых может работать данный проект.
   
## Запуск программы
Запустите программу, выполнив в терминале следующую команду:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

В терминале будет выведено следующее сообщение:
```bash
Performing system checks...

System check identified no issues (0 silenced).
April 15, 2021 - 14:56:04
Django version 1.11.29, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

Откройте в браузере ссылку [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
