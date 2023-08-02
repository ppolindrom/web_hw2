from django.db import models




NULLABLE = {'blank': True, 'null': True}  # константа для необязательного поля


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')
    image = models.ImageField(verbose_name='изображение', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория', blank=True, null=True)
    price = models.IntegerField(verbose_name='цена', blank=True, null=True)
    date_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    date_change = models.DateTimeField(verbose_name='дата изменений', auto_now=True)


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}. {self.text}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'
        ordering = ('title',)

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    text = models.TextField(max_length=10000, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}. {self.text}'

    class Meta:
        verbose_name = 'кетегория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'
        ordering = ('title',)
