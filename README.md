# Тестовое задание для кандидата инженера-разработчика Python
## Front
- Разработать сайт «из одной страницы» с использованием веб-фреймворка Django 2.0 и
Django REST Framework.
- На единственной странице сайта должна быть размещена форма для загрузки файлов (картинок).
- Предусмотреть, по возможности, множественную загрузку файлов, 
отображение динамичного прогресса загрузки. 
- После загрузки картинки, ее необходимо отображать на этой же странице.
- Для картинки должна быть создана «миниатюра» 
- По клику на миниатюру должно происходить скачивание исходной версии картинки.
- Рядом с каждой миниатюрой необходимо расположить «крестик», по клику на который,
картинка и миниатюра удаляются с сервера (и исчезают со страницы сайта).

## API 
- Первый вызов должен отдавать полный список всех картинок, загруженных на сайт. В списке должна присутствовать и мета-информация 	(разрешение изображение, размер и тип файла, ссылки на скачивание миниатюры и
оригинала картинки и тд). 
- Второй вызов должен отдавать элемент по id. 
- Третий вызов должен удалять элемент по id.

Выполненное задание передать в виде django-проекта. Который должен запускаться
(python manage.py runserver 8000) и работать в отладочном режиме. Использование веб-
серверов (nginx, apache) не является необходимым. Использование WSGI серверов также
не является необходимым. Из дополнительных компонентов разрешено использование
redis.