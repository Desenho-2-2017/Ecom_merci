import pytest
from users.models import (PhoneNumber, CustomerUser)
from products.models import (Product, ProductCategory)
from cart.models import (
    Cart,
    # ItemManager,
    # Item
    )
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


@pytest.mark.django_db
def test_product_category():
    category = ProductCategory()
    category.category_name = "Tenis"

    category.save()
    category_count = ProductCategory.objects.all().count()
    assert category_count >= 1
    category.delete()


@pytest.mark.django_db
def test_product():

    category = ProductCategory()
    category.category_name = "Tenis"

    category.save()

    product = Product()

    product.product_name = "Metcon"
    product.category_id = category
    product.stock_quantity = 10
    product.price = 459
    product.weight = 10
    product.width = 20
    product.height = 10
    product.product_type = "Padrao"

    product.save()

    products = Product.objects.all().count()

    assert products >= 1
    product.delete()


@pytest.mark.django_db
def test_cart():

    cart = Cart()

    cart.creation_date = '2010-02-12'
    cart.checked_out = False

    cart.save()
    count_carts = Cart.objects.all().count()

    assert count_carts >= 1
    cart.delete()

#
# @pytest.mark.django_db
# def test_item():
#     cart = Cart()

#     cart.creation_date = '2010-02-12'
#     cart.checked_out = False

#     cart.save()
#     cart.delete()

#     item = ItemManager()

#     item.cart = cart
#     item.quantity = 12
#     item.unit_price = 12.9
#     item.content_type = item.Product()
#     item.object_id = 12
#     item.objects = item.ItemManager()

#     item.save()
#     count_items = Item.objects.all().count()

#     assert count_items >= 1
#     item.delete()
