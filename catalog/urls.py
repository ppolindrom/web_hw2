from django.urls import path
from . import views
from catalog.views import index, contacts

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', contacts),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]



