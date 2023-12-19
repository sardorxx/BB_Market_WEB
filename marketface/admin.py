from django.contrib import admin

# Register your models here.


# Register your models here.

from .models import Product, Category, Comment, ProductAbout, Type

admin.site.register([Category, Comment, ProductAbout, Type])


@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ['name', 'is_deleted']

