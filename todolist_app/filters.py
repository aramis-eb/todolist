import django_filters

from .models import Todo, Priority


class TodoFilter(django_filters.FilterSet):
    priority = django_filters.ModelChoiceFilter(
        queryset=Priority.objects.all()
        )

    class Meta:
        model = Todo
        fields = {
            'tittle': ['icontains'],
            'description': ['icontains'],
            'priority': [],
        }
