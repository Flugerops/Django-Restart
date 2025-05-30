import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from accounts.models import Profile
from products.models import Cart, Product, Category, CartItem
from .fixtures import product, product_with_discount


@pytest.mark.django_db
def test_product_model():
    category = Category.objects.create(name="test_category")
    product = Product.objects.create(
        name="test_product",
        category=category,
        nomenclature="test_nomenclature",
        price=100,
        discount=10,
    )

    assert product.discount_price == 90
    assert product.category.name == "test_category"


@pytest.mark.django_db
def test_cart_model_one_product(user, product):
    cart_item = CartItem.objects.create(cart=user.cart, product=product)
    assert cart_item.item_total == product.price
    assert user.cart.total == product.price


@pytest.mark.django_db
def test_cart_model_diffrent_products(user, product_with_discount, product):

    cart_item = CartItem.objects.create(
        cart=user.cart,
        product=product_with_discount,
    )

    cart_item_2 = CartItem.objects.create(
        cart=user.cart,
        product=product,
    )

    assert user.cart.total == 190
