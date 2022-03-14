from rest_framework import serializers

from shipments.models import Shipments


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipments
        exclude = ("created_at", "updated_at", "delete_at")


class CreateShipmentRequestSerializer(serializers.Serializer):
    order_id = serializers.UUIDField()
    products_to_ship = serializers.ListField(child=serializers.UUIDField())
    address = serializers.CharField(max_length=200)
    cellphone_number = serializers.CharField(max_length=10)
