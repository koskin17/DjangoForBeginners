from django.urls import path

# Импортируем контроллеры
from products.views import products, basket_add

# Обязательно создаётся переменная app_name с названием нашего приложения 'products'. Это позволяет django понимать к какому приложению относятся ниже приведённые маршруты
app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add')
]