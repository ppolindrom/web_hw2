from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение')
    category = models.CharField(verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_creation = models.DateTimeField(verbose_name='дата создания')
    date_change = models.DateTimeField(verbose_name='дата изменений')

    # last_name = models.CharField(max_length=150, verbose_name='фамилия')
    #
    # def __str__(self):
    #     # Строковое отображение объекта
    #     return f'{self.first_name} {self.last_name}'
    #
    # class Meta:
    #     verbose_name = 'студент' # Настройка для наименования одного объекта
    #     verbose_name_plural = 'студенты'