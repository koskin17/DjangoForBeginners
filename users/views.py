from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import auth, messages   # auth - это модуль, который позволяет работать с пользователями, а messages - это модуль, который позволяет выводить кастомные сообщения пользователю

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket

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
            messages.success(request, 'Вы успешно зарегистрированы и можете авторизироваться под своим логином и паролем!')  # Выводим сообщение пользователю, что он успешно зарегистрирован
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    active_user = request.user # Получение пользователя из информации в запросе, чтобы дальше по коду не повторять эту строку.
    # Это POST запрос, который позволяет менять информацию в БД / в профиле
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=active_user)    # Если метод POST, то в форму передаются сами данные метода POST, а также указывается объект, который меняется - instance=request.user, т.е. указывается пользователь, с которым мы будем иметь дело и данные которого будут меняться. Также отдельно и специально передаётся FILE, без чего файл не поменяется
        # Дальше идёт проверка на валидность данных
        if form.is_valid():
            # Если проверка валидности прошла,то форма сохраняется
            form.save()
            # И позвращается редирект, т.е. пользователь перенаправляется на ту страницу, на которой он менял данные, т.е. на профиль.
            return redirect('users:profile')
    else:
        # Это GET запрос, т.е. когда информация получается из БД
        form = UserProfileForm(instance=active_user) # Именно instance = request.user обеспечивает отображение информации пользователя в полях в личном кабинете / в профиле.
    context = {
            'form': form, 'title': 'Store - личный кабинет',
            'baskets': Basket.objects.filter(user=active_user),    # Если указать Basket.objects.all(), то будут видны заказы всех пользователей в корзине конкретного пользователя. По этой причине надо указывать с фильтром по пользователю, которого мы получаем из запроса.
            }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return redirect(request, 'index')
