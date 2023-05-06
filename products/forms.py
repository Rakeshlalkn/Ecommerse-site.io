from django import forms
from .models import Category, Subcategory, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Category Name'}

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
        labels = {'name': 'Subcategory Name', 'category': 'Category'}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'subcategory', 'category','image']
        labels = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': 'Product Price',
            'subcategory': 'Subcategory',
            'category': 'Category',
            'image': 'Image'
        }
        widgets = {
            'categories': CheckboxSelectMultiple(),
            'subcategory': CheckboxSelectMultiple(),
        }
