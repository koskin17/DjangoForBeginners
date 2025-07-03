from django.db import models

# Модели в Django - это обычные классы в Pyton
# Пустой класс или модель в Django создать нельзя. Он всегда унаследован от models.Model.
# Поле id или primary_key в Django создаётся автоматически, если не указано иное.
# Если в качестве primaty_key хочется использовать другое поле, то нужно указать primary_key=True в этом поле и тогда это поле станет первичным ключом модели: name = models.CharField(max_length=64, unique=True, verbose_name='Наименование категории', primary_key=True)
 
class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Наименование категории')    # unique=True означает, что данное поле должно быть уникальным
    description = models.TextField(blank=True, verbose_name='Описание категории')   # Специальный класс для поля с большим кол-вом текста. blant=True позволяет полю быть пустым

class Product(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Наименование товара')
    image = models.ImageField(upload_to='products_images/', blank=True, verbose_name='Изображение товара')  # upload_to - путь к папке, куда будут загружаться изображения. Папка products будет создана в MEDIA_ROOT
    description = models.TextField(blank=True, verbose_name='Описание товара')
    shoort_description = models.CharField(max_length=64, blank=True, verbose_name='Краткое описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара', blank=False, default=0)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара')  # PositiveIntegerField - поле для положительных целых чисел
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', verbose_name='Категория товара')  # Связь с моделью ProductCategory.  on_delete=models.PROTECT охначает, что при удалении категории будут одновременно удалены и все товары ,которые в неё входят. on_delete=models.PROTECT означает, что категорию нельзя удалить пока хотя бы один товар в ней есть. related_name='products' - позволяет получить все товары в категории через category.products.all()
    is_active = models.BooleanField(default=True, verbose_name='Активность товара')