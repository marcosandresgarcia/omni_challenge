import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from users.tests.factories import UserFactory
from orders.choices import STATUS
from orders.models import Orders

ORDER_STATUS = [x[0] for x in STATUS]


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Orders

    user = factory.SubFactory(UserFactory)
    total_order_price = FuzzyInteger(low=100)
    balance = FuzzyInteger(low=100)
    status = FuzzyChoice(ORDER_STATUS)
