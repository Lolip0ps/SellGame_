from django.db import models
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class NameGame(models.Model):
    name = models.TextField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название игры'
        verbose_name_plural = 'Названия игр'


class KeyGame(models.Model):
    name = models.ForeignKey(NameGame, on_delete=models.PROTECT, verbose_name='Название')
    key = models.TextField(max_length=30, verbose_name="Ключ")

    class Meta:
        verbose_name = 'Ключ игры'
        verbose_name_plural = 'Ключи игр'
        ordering = ['name', ]


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Жанр')
    name = models.TextField(verbose_name='Название игры')
    connect = models.ForeignKey(NameGame, on_delete=models.PROTECT, verbose_name='Связь с игрой')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to="game/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField(verbose_name='Осталось')
    Publisher = models.TextField(verbose_name='Издатель')
    Developer = models.TextField(verbose_name='Разработчик')
    release = models.DateField(verbose_name="Дата выхода")
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'
        ordering = ['name', 'time_create']
        index_together = (('name', 'slug'),)

    def __str__(self):
        return self.name
