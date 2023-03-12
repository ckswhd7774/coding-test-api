from django_filters import rest_framework as filters


class AnswerFilter(filters.FilterSet):
    type = filters.CharFilter(method="type_filter")

    @staticmethod
    def type_filter(queryset, name, value):
        if value:
            queryset = queryset.filter(type=value)
        return queryset
