from django.contrib import admin
from users.models import User

#  Импортируем класс отображением товаров в адинке, которые пользователь добавил в корзину
from products.admin import BasketAdminInLine 

# Создаём обычный класс user Admin, который будет наследоваться от admin.ModelAdmin
@admin.register(User)  # Регистрируем модель User с помощью декоратора
class UserAdmin(admin.ModelAdmin):
    inlines = [BasketAdminInLine]  # Добавляем в админку пользователя отображение корзины пользователя
