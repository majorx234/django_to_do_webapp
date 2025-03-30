from django.views.generic import View
from django.shortcuts import render

from todo.models import Task
from todo.tables import ToDoTable


class MainView(View):
    # login_url = '/accounts/login/'
    # permission_required = 'todo.view_todo'
    # filterset_class = TaskFilter
    template_name = 'current_todo.html'
    model = Task
    table_class = ToDoTable

    def get(self, request, *args, **kwargs):
        return render(request,'current_todo.html')
