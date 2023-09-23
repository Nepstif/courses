from django.urls import path

from product.views import get_lesson

app_name = "product"

urlpatterns = [
    path("product", get_lesson, name="product"),

]