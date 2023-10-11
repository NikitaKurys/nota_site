from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    img = models.ImageField(upload_to='static/store/img/category_images', null=True, blank=True, verbose_name='Картинка категории')
    slug = models.SlugField(max_length=40, unique=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Основные категории'
        verbose_name_plural = 'Основные категории'

    def __str__(self):
        return self.name


class SlaveCategory(models.Model):
    main = models.ForeignKey(to=MainCategory, on_delete=models.PROTECT, related_name='maincategory', verbose_name='Категория')
    name = models.CharField(max_length=128, unique=False, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=40, unique=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class ProductCards(models.Model):
    CATEGORY_CHOICES = [
        ("М", "Мужские"),
        ("Ж", "Женские"),
        ("У", "Унисекс"),
    ]

    name = models.CharField(max_length=256, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена товара за 5 мл')
    image = models.ImageField(upload_to='static/store/img/product_images', null=True, blank=True, verbose_name='Картинка товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    gender_name = models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=True, null=True, verbose_name='Гендер')
    category = models.ForeignKey(to=MainCategory, on_delete=models.PROTECT, related_name="products", verbose_name='Категория')
    slave = models.ForeignKey(to=SlaveCategory, on_delete=models.PROTECT, related_name="slave_products", null=True, blank=True, verbose_name='Подкатегория')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class SiteContent(models.Model):

    NAME_CHOICES = [
        ("БФ", "Большая картинка вверху сайта"),
        ("МФ1", "Маленькая картинка вверху сайта (1)"),
        ("МФ2", "Маленькая картинка вверху сайта (2)"),
        ("МФ3", "Маленькая картинка вверху сайта (3)"),
        ("МК1", "Картинка внизу главной страницы"),
        ("МК2", "Картинка на странице контактов"),
        ("ЖТ1", "Жирный текст вверху сайта (1)"),
        ("МТ1", "Маленький текст вверху сайта (1)"),
        ("ЖТ2", "Жирный текст вверху сайта (2)"),
        ("МТ2", "Маленький текст вверху сайта(2)"),
        ("ЖТ3", "Жирный текст вверху сайта (3)"),
        ("МТ3", "Маленький текст вверху сайта (3)"),
        ("ЖТ4", "Жирный текст внизу сайта (4)"),
        ("МТ4", "Маленький текст внизу сайта (4)"),
    ]

    name = models.CharField(max_length=3, choices=NAME_CHOICES, verbose_name='Контент')
    image = models.ImageField(upload_to='static/store/img/content_img', null=True, blank=True,
                              verbose_name='Картинка товара')
    description = models.TextField(null=True, blank=True, verbose_name='Текст')

    class Meta:
        verbose_name = 'Контент сайта'
        verbose_name_plural = 'Контент сайта'

    def __str__(self):
        return self.name