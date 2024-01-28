from django.urls import path
from django.views.decorators.cache import cache_page
from .views import ProductListView, ContactView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, VersionCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/',
         ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/',
         ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/',
         cache_page(60 * 15)(ProductDetailView.as_view()), name='product_detail'),
    path('products/<int:product_id>/create_version/',
         VersionCreateView.as_view(), name='create_version'),
]
