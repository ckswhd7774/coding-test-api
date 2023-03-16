from django_filters import rest_framework as filters


class QuestionFilter(filters.FilterSet):
    category = filters.CharFilter(method="category_filter")

    @staticmethod
    def category_filter(queryset, name, value):
        if value:
            queryset = queryset.filter(category=value)
        return queryset
