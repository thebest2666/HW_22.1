from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED

def get_categories():
    if CACHE_ENABLED:
        key = f'categories'
        categories = cache.get(key)
        if categories is None:
            categories = Category.objects.all()
            cache.set(key, categories)
    else:
        categories = Category.objects.all()
    return categories