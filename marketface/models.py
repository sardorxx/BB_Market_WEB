from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='short')
    image = models.ImageField(upload_to='category_image/', verbose_name='rasm')
    is_deleted = models.BooleanField(default=False, verbose_name='o\'chirilganmi')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='nomi')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='short')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='kategoriya')
    image = models.ImageField(upload_to='type_image/', verbose_name='rasm')
    is_deleted = models.BooleanField(default=False, verbose_name='o\'chirilganmi')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ichki kategoriya'
        verbose_name_plural = 'Ichki kategoriyalar'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='nomi')
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name='short')
    more_about = models.TextField(max_length=255, verbose_name='ta\'rifi')
    price = models.IntegerField(verbose_name='narxi')
    amount = models.IntegerField(default=0, verbose_name='miqdori')
    color = models.CharField(max_length=20, blank=True, null=True, verbose_name='rangi')
    size = models.CharField(max_length=20, blank=True, null=True, verbose_name='razmeri')
    product_guid = models.TextField(max_length=255, blank=True, null=True, verbose_name='foydalanish yo\'riqnomasi')
    image = models.ImageField(upload_to='product_image/', verbose_name='rasm')
    seller = models.CharField(max_length=100, verbose_name='sotuvchi')
    dated = models.DateTimeField(auto_now_add=True, verbose_name='qo\'shilgan vaqt')
    updated = models.DateTimeField(auto_now=True, verbose_name='yangilangan vaqt')
    in_product = models.CharField(max_length=100, verbose_name='qo\'shimcha')
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='ichki kategoriya')
    is_deleted = models.BooleanField(default=False, verbose_name='o\'chirilganmi')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='foydalanuvchi')
    text = models.TextField(null=True, blank=True, verbose_name='sharh')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name='mahsulot')
    image = models.ImageField(upload_to='comments_image/', blank=True, null=True, verbose_name='rasm')
    created = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqt')
    is_deleted = models.BooleanField(default=False, verbose_name='o\'chirilganmi')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.slug = None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.text)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Sharh'
        verbose_name_plural = 'Sharhlar'


class ProductAbout(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='mahsulot')
    rate = models.IntegerField(default=0, verbose_name='baho')
    rated_num = models.IntegerField(default=0, verbose_name='baholar soni')
    ordered_num = models.IntegerField(default=0, verbose_name='buyurtmalar soni')
    liked = models.BooleanField(default=False, verbose_name='sevimli')
    created = models.DateTimeField(auto_now_add=True, verbose_name='yaratilgan vaqt')
    is_deleted = models.BooleanField(default=False, verbose_name='o\'chirilganmi')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.slug = None

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Mahsulot haqida'
        verbose_name_plural = 'Mahsulotlar haqida'
