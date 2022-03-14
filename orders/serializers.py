from rest_framework import serializers

from .models import Orders


class OrderProductDetailsSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    units = serializers.IntegerField()


class OrderProductsListSerializer(serializers.Serializer):
    products = OrderProductDetailsSerializer(many=True)


class OrdersSerializer(serializers.ModelSerializer):
    product_detail = OrderProductDetailsSerializer(many=True, read_only=True)
    class Meta:
        model = Orders
        exclude = ("created_at", "updated_at", "delete_at")

