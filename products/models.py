from django.db import models
from base.models import BaseModel
from django.db.models.signals import post_save
from django.dispatch import receiver



class Products(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion", blank=True, null=True)
    unit_price = models.FloatField(verbose_name="Precio por unidad")


    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def get_units(self):
        try:
            available_units = self.available_units.units
        except Products.available_units.RelatedObjectDoesNotExist: # noqa
            available_units = 0
        return available_units

    def update_units(self, units_to_update):
        product_detail = self.available_units
        if units_to_update >= 0 or product_detail.units + units_to_update >= 0:
            product_detail.units += units_to_update
            product_detail.save()
        else:
            return None
        return product_detail.units



class AvailableProducts(BaseModel):
    product = models.OneToOneField(Products, on_delete=models.CASCADE, related_name="available_units")
    units = models.IntegerField()

    class Meta:
        verbose_name = "Unidad disponible"
        verbose_name_plural = "Unidades disponibles"


@receiver(post_save, sender=Products)
def my_handler(sender, **kwargs):
    product = kwargs["instance"]
    try:
        product.available_units
    except Products.available_units.RelatedObjectDoesNotExist:  # noqa
        AvailableProducts.objects.create(product=kwargs["instance"], units=0)
