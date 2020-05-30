from random import choice
from faker import Faker
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bmg_hacka.settings')
django.setup()
from api.models import User

fake = Faker('pt_BR')
rendas = list([x for x in range(400, 10000, 50)])

for _ in range(200):
    name = fake.name()
    user_name = fake.user_name()
    renda = float(choice(rendas))

    us = User(name=name, user_name=user_name, renda=renda)
    us.save()
