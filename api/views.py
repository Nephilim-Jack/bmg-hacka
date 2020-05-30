from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User, Group

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