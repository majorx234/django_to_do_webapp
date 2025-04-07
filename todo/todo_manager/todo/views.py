from django.views.generic import CreateView, DetailView, View
from django_tables2.views import SingleTableMixin
from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task
from todo.forms import ToDoForm
from todo.tables import ToDoTable


# Create your views here.
class ToDoCreateView(CreateView):
    # permission_required = 'todo.add_task'
    model = Task
    template_name = 'detail.html'
    form_class = ToDoForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        return super().form_valid(form)


class ToDoListView(DetailView):
    # permission_required = 'todo.view_tasks'
    model = Task
    template_name = 'list.html'
    context = {
        "my_item_list": [(1, "fo"), (2, "foo"), (3, "fooo"),
                         (4, "foooo"), (5, "fooooo"), (6, "foooooo"),
                         (7, "fooooooo")],
    }
    #    table_class = ToDoTable

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


class MainView(View):
    # login_url = '/accounts/login/'
    # permission_required = 'todo.view_todo'
    # filterset_class = TaskFilter
    template_name = 'current_todo.html'
    model = Task
    table_class = ToDoTable

    def get(self, request, *args, **kwargs):
        mydict = {}
        mydict['test'] = "foo"
        return render(request, 'current_todo.html', mydict)
