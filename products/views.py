from django.views import View
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse
from .models import Category, Subcategory, Product
from .forms import ProductForm,SubcategoryForm,CategoryForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ProductListView(View):
    template_name = 'product_list.html'
    ajax_template_name = 'ajax_product_list.html'

    def get(self, request):
        category = request.GET.get('category')
        subcategory = request.GET.get('subcategory')

        if category and subcategory:
            products = Product.objects.filter(subcategory__name=subcategory, subcategory__category__name=category)
        elif category:
            products = Product.objects.filter(subcategory__category__name=category)
        elif subcategory:
            products = Product.objects.filter(subcategory__name=subcategory)
        else:
            products = Product.objects.all()

        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        print("products",products)

        context = {
            'products': products,
            'categories': categories,
            'subcategories': subcategories,
            'selected_category': category,
            'selected_subcategory': subcategory,
        }

        if request.is_ajax():
            return render(request, self.ajax_template_name, context)

        return render(request, self.template_name, context)
    

class CategoryCreateView(View):
    template_name = 'category_form.html'

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        return render(request, self.template_name, {'form': form})
    

class CategoryListView(View):
    template_name = 'category_list.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})
    

class SubcategoryCreateView(View):
    template_name = 'subcategory_form.html'

    def get(self, request):
        form = SubcategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
        return render(request, self.template_name, {'form': form})
    

class SubcategoryListView(View):
    template_name = 'subcategory_list.html'

    def get(self, request):
        subcategories = Subcategory.objects.all()
        return render(request, self.template_name, {'subcategories': subcategories})

    


class ProductCreateView(View):
    template_name = 'product_form.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, self.template_name, {'form': form})
    





