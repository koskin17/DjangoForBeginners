"""
Views - это так называемые контроллеры, которые отвечают за работу определённо логики или функций или за отображение определённых шаблонов.
Views - это просто функции, которые вызываются.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Декоратор, который позволяет ограничить доступ к показу страниц только для авторизованных пользователей

from products.models import ProductCategory, Product, Basket

def index(request):
    # В данном случае возвращается результат - функция render, которая и рендерит (создаёт) определённую страницу.
    # В фукнцию render обязательно передаётся первый параметр - request.
    # Для возвращения срендеринной страницу нужно указать сам запрос, который мы передали, и путь к шаблону той страницы, которую мы возвращаем.
    # У нас в папке product есть папка templates и django понимает, что в этой папке лежат шаблоны.
    # Т.е. когда django нужен шаблон из products она сама найдёт папку templates и в ней найдёт шаблон.
    # Для того, чтобы страница отображалась нужно указать путь к ней в файле urls.py в корневой папке приложения.
    context = {
        'title': "Store"
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None):
    """ Method to display all products in the store """
    context = {
        'title': "Store - Каталог",
        'categories': ProductCategory.objects.all(),    # Получаем все категории продуктов из базы данных
    }
    
    if category_id:
        context.update({'products': Product.objects.filter(category_id=category_id)})  # Получаем / фильтруем товары на странице по категории
    else:
        context.update({'products': Product.objects.all()})  # Получаем все товары из всех категория в базе данных
    return render(request, 'products/products.html', context)

@login_required  # Декоратор, который позволяет ограничить доступ к показу страниц только для авторизованных пользователей
def basket_add(request, product_id):
    """ Method to add a product to the basket """
    
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)
    
    if not basket.exists():    # Метод exsists применяется только для списков
        basket = Basket(user=request.user, product=product, quantity=1)
        basket.save()
        # Второй способ создать объект корзины, если его ещё нет у пользователя
        # Basket.objects.create(user=request.user, product=product, quantity=1)
        return redirect(current_page)   # Возвращаем пользователя на ту же страницу, на которой он находится сейчас
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)

def basket_delete(request, id):
    """ Method to delete a product from the basket"""
    
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def test_context(request):
    """ Method to test context data in a template """
    
    context = {
        'title': 'store',
        'header': 'Welcome to our store!',
        'username': 'John Doe',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6990.00,
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {'name': 'Синяя куртка The North Face',
            'price': 23725.00,
            'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
            'price': 3390.00,
            'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ],
        'products_of_promotion': [
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
            'price': 1500.00,
            'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ]
    }
    return render(request, 'products/test-context.html', context)