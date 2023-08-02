from django.db import models

NULLABLE = {'blank': True, 'null': True}  # константа для необязательного поля


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', **NULLABLE)
    category = models.CharField(verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    date_change = models.DateTimeField(verbose_name='дата изменений')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}. {self.text}'

    class Meta:
        verbose_name = 'кетегория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'кадегории'
        ordering = ('title',)

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')
    blabla