# python manage.py shell
# mamy dostęp do ustawień z settings.py projektu
import os
os.environ['DJANGO_SETTINGS_MODULE']
# dostaniemy <project>.settings

# jeśli nie używamy manage.py, to musimy zrobić ręczny import
import django
django.setup()

from polls.models import Question, Choice
Question.objects.all()

# mamy w ustawieniach włączone wsparcie dla stref czasowych
# django oczekuje datetime z tzinfo (DateTimeField)
# zamiast datetime.datetime.now() używamy timezone.now()
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# musimy wywołać explicite save(), bo zapisaliśmy obiekt do zmiennej
q.save()
# teraz obiekt ma id
q.id

# dostęp poprzez atrybuty
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
# możemy użyć metody zdefiniowanej w klasie
q.was_published_recently()

# bogate lookup API bazy danych sterowane keywordami
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

# filter() zwróci QuerySet, a get() obiekt
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
Question.objects.filter(pub_date__year=current_year)

# żądanie id, które nie istnieje, dostaniemy wyjątek
Question.objects.get(id=2)

# wyszukiwanie po kluczu głównym
Question.objects.get(pk=1)

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question
q.choice_set.all()
q.choice_set.count()

# __ separuje relacje
Choice.objects.filter(question__pub_date__year=current_year)

# usuwanie rekordu
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
q.choice_set.all()

# taggit
from blog.models import Post

post = Post.objects.get(id=1)
post.tags.add('music', 'jazz', 'django')
post.tags.all()

post.tags.remove('django')
post.tags.all()

localhost:8000/admin/taggit/tag
localhost:8000/admin/blog/post
