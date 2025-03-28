from django.shortcuts import render

def index(request):
    # В данном случае возвращается результат функции render - она рендерит определённую страницу
    # В фукнцию render обязательно передаётся первый параметр - request и второй параметр - template name или путь к шаблону,
    # который нужно отрендерить / отобразить
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')
