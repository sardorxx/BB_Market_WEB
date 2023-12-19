from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.db import models

from marketface.models import ProductAbout, Product


# Create your models here.


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField('Email:', unique=True, null=True, blank=True)
    phone = models.CharField('Phone_number', max_length=13)
    image = models.ImageField(upload_to='users_image/', blank=True, null=True)
    sex = models.CharField(max_length=10)
    birth_date = models.DateField(blank=True, null=True)
    liked_products = models.ManyToManyField(ProductAbout)
    basket = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        help_text=
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        help_text='Specific permissions for this user.',
    )
