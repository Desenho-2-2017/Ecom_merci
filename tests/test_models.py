import pytest
from users.models import (PhoneNumber, CustomerUser)

# Remenber to use test_TESTNAME.py


@pytest.mark.django_db
def test_phone_number():

    phone_number = PhoneNumber()

    phone_number.phone = '33576474'

    phone_number.save()
    count_phone_numbers = PhoneNumber.objects.all().count()

    assert count_phone_numbers >= 1
    phone_number.delete()


@pytest.mark.django_db
def test_customer_user():

    phone_number = PhoneNumber()
    phone_number.phone = '33576474'
    phone_number.save()

    phone_number2 = PhoneNumber()
    phone_number2.phone = '12345678'
    phone_number2.save()

    phone_number3 = PhoneNumber()
    phone_number3.phone = '87654321'
    phone_number3.save()

    user = CustomerUser()

    user.name = 'Gabriela'
    user.last_name = 'Gama'
    user.set_password('123456')
    user.email = 'gaby@mail.com'
    user.save()
    user.phone_numbers.add(phone_number)
    user.phone_numbers.add(phone_number2)
    user.phone_numbers.add(phone_number3)
    user.save()

    count_users = CustomerUser.objects.filter(pk=user.pk).count()

    assert count_users >= 1
    user.phone_numbers.remove(phone_number)
    user.phone_numbers.remove(phone_number2)
    user.phone_numbers.remove(phone_number3)
    phone_number.delete()
    phone_number2.delete()
    phone_number3.delete()
    user.delete()
