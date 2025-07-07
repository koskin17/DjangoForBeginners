"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Импортируется include для пространства имён
from django.conf.urls.static import static
from django.conf import settings

from products.views import index, test_context   # Импорт функции из файла products/views.py

# В urlpattern первым параметров указывается адрес, по которому будет отображаться страница,  а вторым - сама страница, которая будет отображаться
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),   # Путь к главной странице сайта. Из-за пустого первого параметра ('') при переходе на наш сайт / проект будет открываться наша главная старница, которую мы описали как index и которая вызывается функцией index из файла products/views.py
    path('products/', include('products.urls', namespace='products')),  # Путь к странице с товарами. В этом случае мы хотим, чтобы наша страница products открывалась по url-адресу со словом "products/" и из-за этого мы это указываем в качестве первого параметра в ''. При переходе на наш сайт / проект будет открываться страница с товарами, которую мы описали как products и которая вызывается функцией products из файла products/views.py.
    # Также тут примененно пространство имён и все маршруты с products теперь имеют пространство имён "products" и обрабатываются приложением products
    path('test-context/', test_context, name = 'test_context'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Добавляем обработку медиафайлов в режиме отладки. Это нужно для того, чтобы при отладке проекта можно было видеть изображения, которые мы загружаем в папку media
    # MEDIA_URL - это URL-адрес, по которому будут доступны медиафайлы
    # MEDIA_ROOT - это путь к папке, где будут храниться медиафайлы
