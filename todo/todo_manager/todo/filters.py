from todo.models import Task
from django_filters import FilterSet, DateFilter
from bootstrap_datepicker_plus.widgets import DatePickerInput


class TaskFilter(FilterSet):
    till_when_date__gte = DateFilter(
        field_name='till_when_date',
        lookup_expr='gte',
        input_formats=["%Y-%m-%d"],
        label='start date...',
        widget=DatePickerInput(
                    options={
                        "format": "YYYY-MM-DD",
                        "showClose": True,
                        "showClear": True,
                        "showTodayButton": True,
                    }
                            ))
    till_when_date__lte = DateFilter(
        field_name='till_when_date',
        lookup_expr='lte',
        input_formats=["%Y-%m-%d"],
        label='...end Datum',
        widget=DatePickerInput(
                    options={
                        "format": "YYYY-MM-DD",
                        "showClose": True,
                        "showClear": True,
                        "showTodayButton": True,
                    }
                              ))

    class Meta:
        model = Task
        fields = {
            'shorttext': ['icontains', ],
            'status': ['exact', ],
            'list_items': ['exact', ],
        }
