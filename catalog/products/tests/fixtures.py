import pytest

from products.models import Category, Product


@pytest.fixture
def product():
    category = Category.objects.create(name="test-category")
    return Product.objects.create(
        name="test-product",
        category=category,
        nomenclature="test-nomenclature",
        price=100,
    )


@pytest.fixture
def product_with_discount():
    category = Category.objects.create(name="test-category_2")

    return Product.objects.create(
        name="test_product",
        category=category,
        nomenclature="test-nomenclature_2",
        price=100,
        discount=10,
    )
