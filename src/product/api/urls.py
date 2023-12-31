from django.urls import path

from . import views

app_name = "product"


urlpatterns = [
    path('product/',
         views.ProductListView.as_view(),
         name='product_list'),
    path('product/<pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),
]