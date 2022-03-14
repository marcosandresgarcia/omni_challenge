import factory
from factory.fuzzy import FuzzyChoice

from orders.tests.factories import OrderFactory
from users.tests.factories import UserFactory
from shipments.choices import STATUS
from shipments.models import Shipments

SHIPMENT_STATUS = [x[0] for x in STATUS]


class ShipmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shipments

    address = factory.Faker('address')
    cellphone_number = factory.Faker('msisdn')
    order = factory.SubFactory(OrderFactory)
    user = factory.SubFactory(UserFactory)
    status = FuzzyChoice(SHIPMENT_STATUS)
