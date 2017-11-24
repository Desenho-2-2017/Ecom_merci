import pytest
from products.models import ProductCategory
from cart.models import (
    Cart,
    # ItemManager,
    # Item
    )
from users.models import (CustomerUser, CreditCard)
# Remenber to use test_TESTNAME.py


@pytest.mark.django_db
def test_customer_user():
    user = CustomerUser()
    user.name = 'Gabriela'
    user.last_name = 'Gama'
    user.set_password('123456')
    user.email = 'gaby@mail.com'
    user.phone_number = '98765432'
    user.cellphone = '123454657'
    user.save()

    count_users = CustomerUser.objects.filter(pk=user.pk).count()

    assert count_users >= 1
    user.delete()


@pytest.mark.django_db
def test_product_category():
    category = ProductCategory()
    category.category_name = "Tenis"

    category.save()
    category_count = ProductCategory.objects.all().count()
    assert category_count >= 1
    category.delete()


# @pytest.mark.django_db
# def test_product():
#
#     category = ProductCategory()
#     category.category_name = "Tenis"
#
#     category.save()
#
#     product = Product()
#
#     product.product_name = "Metcon"
#     product.category_id = category
#     product.stock_quantity = 10
#     product.price = 459
#     product.weight = 10
#     product.width = 20
#     product.height = 10
#     product.product_type = "Padrao"
#
#     product.save()
#
#     products = Product.objects.all().count()
#
#     assert products >= 1
#     product.delete()


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


@pytest.mark.django_db
def test_credit_card():
    user = CustomerUser()
    user.name = 'Gabriela'
    user.last_name = 'Gama'
    user.set_password('123456')
    user.email = 'gaby@mail.com'
    user.phone_number = '98765432'
    user.cellphone = '123454657'
    user.save()

    credit_card = CreditCard()
    credit_card.owner_name = 'Celine Dion'
    credit_card.card_number = '9078563421345678'
    credit_card.security_code = '459'
    credit_card.user = user
    credit_card.expire_date = '2023-08-10'
    credit_card.provider = 'visa'
    credit_card.save()

    count = CreditCard.objects.filter(pk=credit_card.pk).count()
    assert count >= 1
    credit_card.delete()
