from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST': # Проверяем, если метод POST
        form = UserLoginForm(data=request.POST) # То в переменную form собираем данные из пришедшего запроса
        
        if form.is_valid(): # Проверяем получаенные данные на валидность. В этом случае проверка минимальная, просто что оба поля заполнены и не более.
            username = request.POST['username'] # Если данные валидные, то в username вытаскиваем username из данных метода POST
            password = request.POST['password'] # В password вытаскиваем password из данных метода POST
            user = auth.authenticate(username = username, password = password)
            
            # Дальше проверка на то, что пользователь есть и пользователь артивный
            if user and user.is_active: # Поле is_active - это поле по умолчанию в класса AbstractBaseUser, от которого мы наследовали класс User. Оно булевое и используется чтобы не удалять никаких пользователей из БД, а просто отделить старых пользователей от новых или пользователь может сам удалиться, но информация о том, что он был зарегистрирован остаётся и этим "флагом" можно помечать активных пользователей и не активных, чтобы никого не удалять.
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index')) # Перенаправляем пользователя на страницу. Лучше это делать при помощи функции reverse: указывается имя страницы, а она уже сама формирует путь к ней.
            else:
                print(form.errors)
    else:
        form = UserLoginForm()  # В противно случае (если метод не POST), то просто создаётся форма или объект класса UserLoginForm
        
    context = {'form': form} # Форме присваивается имя, чтобы потом в html-шаблоне её можно было вызвать по этому имени.
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)
