from django.urls import path

from product.views import get_lesson

urlpatterns = [
    path("product", get_lesson, name="lesson"),

]