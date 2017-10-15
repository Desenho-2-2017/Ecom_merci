# Remenber to use test_TESTNAME.py
from users.models import *
import pytest

@pytest.mark.django_db
def test_PhoneNumber():

    phone_number = PhoneNumber()

    phone_number.phone = '33576474'

    phone_number.save()
    phone_numbers = PhoneNumber.objects.all().count()

    assert phone_numbers >= 1
    phone_numbers.delete()

@pytest.mark.django_db
def test_CustomerUser():

    user = CustomerUser()

    user.phone_numbers = '33576474'
    user.name = 'Gabriela'
    user.last_name = 'Gama'
    user.set_password('123456')
    user.email = 'gaby@mail.com'
    user.save()

    users = CustomerUser.objects.all().count()

    assert users >= 1
    users.delete()
