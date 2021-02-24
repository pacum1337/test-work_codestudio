import os

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField


def validate_image(fieldfile_obj):
    # size validate
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Максимальный размер фото - {megabyte_limit} Мб")

    # format validate
    extension = os.path.splitext(fieldfile_obj.path)[len(os.path.splitext(fieldfile_obj.path))-1]
    if extension != ".jpg" and extension != ".jpeg":
        raise ValidationError("Формат фото должен быть jpg или jpeg")


class SliderPhoto(models.Model):
    # Изображения слайдера

    name = models.CharField("Название", max_length=100)
    image = ImageField('Избражение', upload_to='slider/', validators=[validate_image])

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'

    def __str__(self):
        return self.name


class HomePageContent(models.Model):
    # Контент домашней страницы
    title = models.CharField("Название вкладки в браузере(Тайтл)", max_length=100, blank=True, null=True)
    keywords = models.TextField('Ключевые слова', blank=True, null=True)
    header_description = models.TextField('Описание', blank=True, null=True)

    header = models.CharField('Заголовок H1', max_length=100)
    slider_images = models.ManyToManyField(SliderPhoto, verbose_name='Фотографии слайдера',
                                           related_name='slider_images', blank=True)
    description = models.TextField('Текст под слайдером', blank=True, null=True)
    map_latitude = models.CharField('Широта карты', max_length=10, blank=True, null=True, default='55.76')
    map_longitude = models.CharField('Долгота карты', max_length=10, blank=True, null=True, default='37.64')

    class Meta:
        verbose_name = 'Контент домашней страницы'
        verbose_name_plural = 'Контент домашней страницы'


class ProductInfoItems(models.Model):
    # Пункты информации о продукте
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт информации о продукте'
        verbose_name_plural = 'Пункты информации о продукте'


class Product(models.Model):
    # Продукция
    title = models.CharField("Название вкладки в браузере(Тайтл)", max_length=100, blank=True, null=True)
    keywords = models.TextField('Ключевые слова', blank=True, null=True)
    header_description = models.TextField('Описание', blank=True, null=True)
    name = models.CharField("Название", max_length=100)
    image = ImageField("Изображение", upload_to='product_images/', validators=[validate_image], blank=True, null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    slug = models.SlugField('URL продукта', max_length=40, default='', unique=True)
    product_info_1 = models.CharField("Заголовок списка 1", max_length=100, blank=True, null=True)
    product_info_items_1 = models.ManyToManyField(ProductInfoItems, verbose_name='Пункты к заголовку 1',
                                                  related_name='product_info_items_1', blank=True)
    product_info_2 = models.CharField("Заголовок списка 2", max_length=100, blank=True)
    product_info_items_2 = models.ManyToManyField(ProductInfoItems, verbose_name='Пункты к заголовку 2',
                                                  related_name='product_info_items_2', blank=True)
    product_info_3 = models.CharField("Заголовок списка 3", max_length=100, blank=True)
    product_info_items_3 = models.ManyToManyField(ProductInfoItems, verbose_name='Пункты к заголовку 3',
                                                  related_name='product_info_items_3', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"
