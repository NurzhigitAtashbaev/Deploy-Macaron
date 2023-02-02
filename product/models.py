from django.db import models


class Raiting:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5

    ALL = (
        (one, '⭐️'),
        (two, '⭐⭐'),
        (three, '⭐⭐⭐'),
        (four, '⭐⭐⭐⭐'),
        (five, '⭐⭐⭐⭐⭐')
    )


class Product(models.Model):
    title = models.CharField(unique=True, max_length=50, primary_key=True, )
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=1770, null=True)
    price = models.CharField(max_length=4, null=True)
    raiting = models.PositiveSmallIntegerField(choices=Raiting.ALL, null=True)
    image = models.OneToOneField('Image', null=True, blank=True, on_delete=models.CASCADE)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='product-images')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
