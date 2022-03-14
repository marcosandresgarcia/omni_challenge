from django.db import models
from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ("created_at", "updated_at", "delete_at")


class CreatePaymentRequestSerializer(serializers.Serializer):
    order_id = serializers.UUIDField()
    amount = serializers.FloatField()
