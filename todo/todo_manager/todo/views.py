from django.views.generic import CreateView, DetailView, \
                                 UpdateView, ListView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from rest_framework import generics

from todo.models import Task
from todo.forms import ToDoForm
from todo.tables import TaskTable
from todo.filters import TaskFilter
from todo.serializers import TaskSerializer


# Create your views here.
class ToDoCreateView(CreateView):
    # permission_required = 'todo.add_task'
    model = Task
    template_name = 'create.html'
    form_class = ToDoForm
    # success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['METHOD'] = 'create'
        return context


class ToDoDetailView(DetailView):
    # permission_required = 'todo.view_tasks'
    model = Task
    template_name = 'detail.html'


class ToDoRestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ToDoListView(SingleTableMixin, FilterView):
    # permission_required = 'todo.view_tasks'
    template_name = 'list.html'
    model = Task
    filterset_class = TaskFilter
    table_class = TaskTable


class ToDoRestListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ToDoUpdateView(UpdateView):
    model = Task
    template_name = 'todo_update.html'
    form_class = ToDoForm
    # fields = [""]
    success_url = '/'


class MainView(SingleTableMixin, FilterView):
    filterset_class = TaskFilter
    template_name = 'current_todo.html'
    model = Task
    table_class = TaskTable
