from django.urls import path
from .views import CategoryCreateView, CategoryListView, SubcategoryCreateView, SubcategoryListView,ProductListView,ProductCreateView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('subcategory/list/', SubcategoryListView.as_view(), name='subcategory_list'),
]