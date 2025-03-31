from django.forms import ModelForm, DateField
from todo.models import Task
from bootstrap_datepicker_plus.widgets import DatePickerInput


class ToDoForm(ModelForm):
    till_when_date = DateField(input_formats=["%Y-%m-%d"], label="till when",
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
        fields = (
            'id',
            'shorttext',
            'longtext',
            'till_when_date',
            'status',
            'list_items',
        )
    def print_todo(self):
        print("print_todo(): here")
        pass
