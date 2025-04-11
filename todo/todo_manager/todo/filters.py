from todo.models import Task
from django_filters import FilterSet, DateFilter
from bootstrap_datepicker_plus.widgets import DatePickerInput


class TaskFilter(FilterSet):
    till_when_date__gte = DateFilter(
        field_name='till_when_date',
        lookup_expr='gte',
        input_formats=["%d.%m.%Y"],
        label='start date...',
        widget=DatePickerInput(
            options={"format": "DD.MM.YYYY",
                     "showClose": True,
                     "showClear": True,
                     "showTodayButton": True,
                     }
        ).start_of('till_when'))

    till_when_date__lte = DateFilter(
        field_name='till_when_date',
        lookup_expr='lte',
        input_formats=["%d.%m.%Y"],
        label='...end Datum',
        widget=DatePickerInput(
            options={"format": "DD.MM.YYYY",
                     "showClose": True,
                     "showClear": True,
                     "showTodayButton": True,
                     }
        ).end_of('till_when'))

    class Meta:
        model = Task
        fields = {
            'shorttext': ['icontains', ],
            'status': ['exact', ],
            'list_items': ['exact', ],
        }
