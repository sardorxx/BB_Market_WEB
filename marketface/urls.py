from django.urls import path
from .views import category_product

app_name = 'marketface'

urlpatterns = [
    path('', category_product, name='home')

]
