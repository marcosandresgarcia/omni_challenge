from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from base.models import BaseModel
from orders.choices import PENDING_PAYMENT, PENDING_SHIPPING, OPEN
from orders.models import Orders
from .choices import STATUS, PENDING, SUCCESSFUL


class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name="payments")
    amount = models.FloatField()
    status = models.CharField(max_length=30, choices=STATUS)

    class Meta:
        db_table = "payments"

    def set_payment_detail(self, order, amount):
        return PaymentDetail.objects.create(payment=self, order=order, amount=amount)


class PaymentDetail(BaseModel):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="payment_detail")
    order = models.ForeignKey(Orders, on_delete=models.PROTECT, related_name="payment_detail")
    amount = models.FloatField()

    class Meta:
        db_table = "payment_details"
        unique_together = (("payment", "order"),)


@receiver(post_save, sender=Payment)
def update_order_post_save(sender, **kwargs):
    payment = kwargs["instance"]
    payment_details = payment.payment_detail.all()
    for payment_detail in payment_details:
        order = payment_detail.order
        if payment.status == PENDING:
            order.balance -= payment.amount
            order.status = PENDING_PAYMENT
        if payment.status == SUCCESSFUL and order.balance == 0:
            count = 0
            payments = order.payment_detail.all()
            for payment_by_order in payments:
                if payment_by_order.payment.status == SUCCESSFUL:
                    count += 1
            if count == len(payments):
                order.status = PENDING_SHIPPING
        else:
            order.status = PENDING_PAYMENT
        order.save()


@receiver(pre_delete, sender=Payment)
def update_order_pre_delete(sender, **kwargs):
    payment = kwargs["instance"]
    payment_details = payment.payment_detail.all()
    for payment_detail in payment_details:
        order = payment_detail.order
        order.status = OPEN
        order.balance += payment.amount
        order.save()


@receiver(post_save, sender=PaymentDetail)
def update_order_post_save(sender, **kwargs):
    payment_detail = kwargs["instance"]
    order = payment_detail.order
    if payment_detail.payment.status == PENDING:
        order.balance -= payment_detail.payment.amount
        order.status = PENDING_PAYMENT
        order.save()
