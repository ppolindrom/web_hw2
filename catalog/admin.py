from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','text')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    list_filter = ('category',)  # Добавляем фильтр по категории
    search_fields = ('title', 'text',)  # Поля для поиска по названию и описанию

# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
