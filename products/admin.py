from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)
# admin.site.register(Product) # Сначала мы в этой строке просто регистрировали модель Product, но затем мы создали класс ProductAdmin и теперь регистрируем его
admin.site.register(Basket)

@admin.register(Product)    # Это альтернативный способ регистрации модели Product с использованием декоратора
class  ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category') # Это список полей, которые будут отображаться в админке
    fields = ('category', ('name', 'image'), ('description', 'short_description'), ('price', 'quantity')) # Если хочется, чтобы какие-то поля были объединенны в одну строку в адинке, то эти поля просто заключаются в скобки, т.е. делается кортеж из них или обхединить в квадратные скобки [], т.е. сделать список. На порядок полей на странице влияет их порядок перечисление в fields
    readonly_fields = ('short_description',) # Эти поля становятся закрытыми для редактирования даже в админке
    ordering = ('name',) # Это порядок сортировки в админке, например по алфавиту. Если добавить минус "-name", то будет обратный порядок сортировки
    search_fields = ('name', 'description') # Это поля, по которым будет осуществляться поиск в админке. Поле поиска появится одно, но искать оно будет по перечисленным полям
    
# Если в админке в карточке пользователя хочется видеть все товары, которые он добавил в корзину, то сначала создаём класс
class BasketAdminInLine(admin.TabularInline):
    model = Basket  # Указываем модель, с которой будем рабоать и из которой будем брать данные
    fields = ('product', 'quantity', 'created_timestap')  # Это поля, которые будут отображаться из указанной модели
    readonly_fields = ('product', 'created_timestap',)
    extra = 0  # Это количество пустых строк, которые будут добавлены в админке для добавления новых товаров в корзину. Если указать 1, то будет одна пустая строка, если 0, то не будет пустых строк