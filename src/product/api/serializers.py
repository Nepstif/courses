from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для данных о продукте
    """

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "access",
            "user",
        ]