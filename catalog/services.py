from django.core.cache import cache

from djangosky.settings import CACHE_ENABLED

from .models import Category, Product


def product_list():
    """
    Возвращает список всех продуктов.
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    cache_key = "products"
    products = cache.get(cache_key)
    if products is None:
        products = Product.objects.all()
        cache.set(cache_key, products, 60 * 10)
    return products


def products_list_for_category(category_id):
    """
    Возвращает список продуктов для указанной категории.
    """
    if not CACHE_ENABLED:
        return Product.objects.filter(category=Category.objects.get(pk=category_id))
    cache_key = "category"
    products = cache.get(cache_key)
    if products is None:
        products = Product.objects.filter(category=Category.objects.get(pk=category_id))
        cache.set(cache_key, products, 60 * 10)
    return products
