"""
Views - это так называемые контроллеры, которые отвечают за работу определённо логики или функций или за отображение определённых шаблонов.
Views - это просто функции, которые вызываются.
"""

from django.shortcuts import render

def index(request):
    # В данном случае возвращается результат - функцию render, которая и рендерит (создаёт) определённую страницу.
    # В фукнцию render обязательно передаётся первый параметр - request.
    # Для возвращения срендеринной страницу нужно указать сам запрос, который мы передали, и путь к шаблону той страницы, которую мы возвращаем.
    # У нас в папке product есть папка templates и django понимает, что в этой папке лежат шаблоны.
    # Т.е. когда django нужен шаблон из products она сама найдёт папку templates и в ней найдёт шаблон.
    # Для того, чтобы страница отображалась нужно указать путь к ней в файле urls.py в корневой папке приложения.
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def test_context(request):
    context = {
        'title': 'store',
        'header': 'Welcome to our store!',
        'username': 'John Doe',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                    'price': 6990.00,
                    'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'name': 'Синяя куртка The North Face',
                    'price': 23725.00,
                    'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': 3390.00,
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ],
        'products_of_promotion': [
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': 1500.00,
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            }
        ]
    }
    return render(request, 'products/test-context.html', context)