# nie jest to konieczne w tests.py
from django.test.utils import setup_test_environment

# instalujemy renderer szablonów, który pozwala badać atrybuty response
# ta metoda nie tworzy na testowej bazie danych
setup_test_environment()

# w tests.py korzystamy z django.test.TestCase, która ma swojego klienta
from django.test import Client
client = Client()

response = client.get('/')
response.status_code

# unikamy kodowania urli na stałe
from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']
