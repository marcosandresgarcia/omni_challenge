import factory
from factory.fuzzy import FuzzyInteger, FuzzyChoice

from users.tests.factories import UserFactory
from payments.choices import STATUS
from payments.models import Payment

PAYMENT_STATUS = [x[0] for x in STATUS]
class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    user = factory.SubFactory(UserFactory)
    amount = FuzzyInteger(low=100)
    status = FuzzyChoice(PAYMENT_STATUS)

