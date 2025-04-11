from django_tables2 import Table, Column
from django.utils.html import format_html
from django.utils.timezone import datetime

from todo.models import Task


class TaskTable(Table):
    id = Column(visible=False)
    longtext = Column(visible=False)

    def render_shorttext(self, record, value):
        url = Task.objects.get(pk=record.id).get_absolute_url()
        html = format_html('<a href="{}">{}</a>', url, value)
        return html

    def render_till_when_date(self, record, value):
        today = datetime.now().date()
        value_date = value.strftime("%d.%m.%Y")
        if value < today:
            html = format_html('<span class="text-danger">{}</span>', value_date)
        else:
            html = value_date
        return html

    class Meta:
        model = Task
        per_page = 20
        order_by = ('till_when_date',)
        attrs = {"class": "table table-striped",
                 "thead": {
                     "class": "thead-light"
                    }
                 }
