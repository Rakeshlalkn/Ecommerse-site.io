from django.urls import path
from .views import CategoryCreateView, ItemsListView, SubcategoryCreateView,ProductListView,ProductCreateView

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('subcategory/create/', SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('product-list', ProductListView.as_view(), name='product_list'),
    path('items/list/', ItemsListView.as_view(), name='item_list'),
]
