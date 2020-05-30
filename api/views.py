from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Group

from random import choice
from faker import Faker

# Create your views here.
def get_groups(request):
    if request.method == 'GET':

        groups = {'groups': list()}
        # Adding groups to the dict
        for gp in Group.objects.all():
            users = list()
            for user in gp.users.all():
                users.append(user.pk)
            act = {
                'code': gp.code,
                'users': users,
                'taxa': gp.taxa
            }
            groups['groups'].append(act)

        return JsonResponse(groups, json_dumps_params={'ensure_ascii': False})


def get_user(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        user = {
            'name': user.name,
            'user_name': user.user_name,
            'renda': user.renda
        }

        return JsonResponse(user, json_dumps_params={'ensure_ascii': False})

def populate(request):
    if request.method == 'GET':
        fake = Faker('pt_BR')
        rendas = list([x for x in range(400, 10000, 50)])

        for _ in range(200):
            name = fake.name()
            user_name = fake.user_name()
            renda = float(choice(rendas))

            us = User(name=name, user_name=user_name, renda=renda)
            us.save()
        return HttpResponse('succefuly populated the database')
