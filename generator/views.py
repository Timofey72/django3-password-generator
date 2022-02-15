from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))
    the_password = ''

    # Проверка, чтобы длина пароля была не больше 14 и не меньше 6
    if length > 14:
        for x in range(14):
            the_password += random.choice(characters)
    elif length < 6:
        for x in range(6):
            the_password += random.choice(characters)
    else:
        for x in range(length):
            the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})


def about_me(request):
    return render(request, 'generator/about_me.html')
