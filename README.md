Требования к заданию:
1. Структура административной панели:
1) вход (по ссылке адрес_сайта/admin);
2) разводящая страница — редактирование главной и редактирование продуктов;
3) редактирование главной в виде списка полей и форм для редактирования контента главной страницы;
4) редактирование продуктов состоит из двух подстраниц: список продуктов (напротив каждого продукта кнопка удаления и изменения) и редактирование страницы продукта в виде списка полей и форма. 
2. Главная страница (index.html):
1) редактирование заголовка главной страницы;
2) загрузка и удаление фотографий слайдера главной страницы;
3) редактирование текста под слайдером с возможность разрывов между абзацами;
4) задание координат на метке карты (в верстке координаты зашиты в div с названием id map);
5) список продуктов выгружается автоматически по дате добавления продуктов.
3. Список продуктов: возможность удаления с подтверждением и добавления нового продукта.
4. Страница продукта:
1) редактирование названия продукта;
2) загрузка и удаление фотографии;
3) возможность редактирования заголовка списков (их будет максимум 3, минимум — 1), а также пунктов списков (количество пунктов не ограничено, поэтому должна быть возможность удалить, редактировать и добавить новые пункты).
5. Как должны происходить загрузка фотографий:
1) все загружаемые фотографии после обработки должны быть точно таких пропорций, как в верстке (обратите внимание, что в слайдере и внутренней странице продукта разные размеры);
2) при загрузке фотографии она автоматически подрезается под нужные размеры, независимо от того, меньше фотография или нет относительно заданных параметров;
3) если произошла ошибка при загрузке, необходимо выводить, что пошло не так, ограничения по размеру 2 Мб, только jpg/jpeg;
4) пример логики загрузки: пользователь загружает фото размером 500x500, происходит автоматический ресайз фото по ширине до необходимых пропорций, затем происходит обрезка фотографии по нижней и верхней части.
6. Работа с текстовыми полями:
1) весь контент, который выгружается в текстовые поля, должен быть без стилей, т.е. применяются только те стили, которые есть на сайте;
2) при создании абзаца (например, в случае текста на главной странице) он должен создаваться автоматически путем подстановки тега <p></p> (смотреть, как это сделано на верстке).
7. Необходимо сделать отправку сообщения с формы любым способом (не обязательно через ajax или smtp-сервер, главное, чтобы сообщение просто отправлялось), сообщения отправляются на почту test@codestudio.org.
8. На всех страницах необходима возможность изменения:
1) тегов keywords и description (в верстке сейчас пустые);
2) тега title;
3) URL страницы (например, чтобы продукт можно было назвать name_product и он открывался по ссылке адрес_сайта/name_product).
9. По всем страницам должна быть возможность сохранения страниц без заполненного контента. Обязательным являются только поля: заголовок страницы и URL-адрес.
10. Варианты демонстрации результата (важный пункт!):
1 вариант, который даст вам значительное преимущество — выгрузка на хостинг Timeweb (https://timeweb.com/ru/services/hosting/). Хостинг бесплатный первые 10 дней и этого хватит для демонстрации результата. Плюс это покажет ваши возможности по настройке хостинга/сервера, что является важным для вакансии. Инструкция по установке и запуску Django на Timeweb здесь: https://timeweb.com/ru/help/display/DOC/Django.
2 вариант, наименее приоритетный — выгрузка в Heroku.
3 вариант, любой другой, но который также в любом случае предполагает отправку нам ссылки для демонстрации результата без установки на локальный сервер для тестирования.
Другие варианты демонстрации результата не принимаются, т.к. мы хотим увидеть ваши навыки не только в реализации, но и в запуске проекта.
