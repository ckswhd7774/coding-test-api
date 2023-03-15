from django.core.cache import cache


def cache_get_queryset(key_prefix):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            key = f"{key_prefix}"
            queryset = cache.get(key)
            if queryset is None:
                queryset = func(self, *args, **kwargs)
                cache.set(key, queryset, timeout=86400)
            return queryset

        return wrapper

    return decorator
