from django.core.cache import cache
from .models import Category


def get_categories():
    categories = Category.objects.all()

    cache_key = 'categories_cache_key'
    cached_categories = cache.get(cache_key)
    if cached_categories is None:
        cached_categories = list(categories)
        cache.set(cache_key, cached_categories, 60 * 15)

    return cached_categories
