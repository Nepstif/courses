"""
Функции панели управления для приложения "Продукт".
"""

from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "access",
        "user",
    )

    search_fields = ("name", "user")

    list_filter = (
        "created_at",
        "updated_at",
    )

    def get_queryset(self, request):
        return Product.objects.select_related("user")
