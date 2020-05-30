#создать проект в cmd
django-admin startproject mysite
django-admin startproject bookmarks

#настройки
settings.py

#запуск сервера
python manage.py runserver #можно указать порт/ip

ctrl+c №завершение работы приложения

#создать приложение
python manage.py startapp articles 

#перенос приложения в mysite\apps
#settings.py
import sys
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0,ps.path.join(PRoJECT_ROOT,'apps'))

#правим urls.py, views, models

#Миграции
settings.py - installed apps
INSTALLED_APPS = ['articles.apps.ArticlesConfig'
python manage.py makemigrations articles
#узнать sql код миграции
python manage.py sqlmigrate articles 0001
#применить миграции
python manage.py migrate

#запросы к БД
python manage.py shell
from articles.models import Article, Comment
from django.utils import timezone
Article.objects.all()
a = Article(article_title = "Какая-то статья", article_text = "Текст статьи", pub_date = timezone.now())
a.save()

a = Article.objects.get(id=1)
a.was_published_recently()

Article.objects.filter(id=1)
Article.objects.filter(article_title__startswith = 'Какая-то')

a.article_title = 'как прошить PS3'


current_year = timezone.now().year
Article.objects.filter(pub_date__year = current_year)

a.comment_set.all()

a.comment_set.create(author_name = "Джек", comment_text = "Крутая статья")
a.comment_set.create(author_name = "Джон", comment_text = "Норм")
a.comment_set.create(author_name = "Волк", comment_text = "ЗБС")
a.comment_set.create(author_name = "Стрелок", comment_text = "ЗБС")

a.comment_set.count()

a.comment_set.filter(author_name__startswith = 'Дж')

cs = a.comment_set.filter(author_name__startswith = 'Дж')
cs.delete()

#использование админки
python manage.py createsuperuser
#перевести админку
settings.py
LANGUAGE_CODE = 'en-us'
#добавляем изменения в admin.py
from .models import Article, Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)


#изменить шаблон админки
https://grappelliproject.com/

settings.py
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

#добавляем views
#изменяем папку где хранятся шаблоны в settings.py
TEMPLATES/DIRS: [os.path.join(PROJECT_ROOT,'templates')]

создаем шаблоны и их расширения






