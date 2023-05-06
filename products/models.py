from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products')
    subcategories = models.ManyToManyField(Subcategory, related_name='products')

    def __str__(self):
        return self.name

