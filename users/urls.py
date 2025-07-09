from django.urls import path

# Импортируем контроллеры
from users.views import login, register, profile

# Обязательно создаётся переменная app_name с названием нашего приложения 'products'. Это позволяет django понимать к какому приложению относятся ниже приведённые маршруты
app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),    
]