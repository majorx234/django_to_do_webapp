from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView

from todo.models import Task
from todo.forms import ToDoForm

# Create your views here.
class ToDoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'todo.add_task'
    model = Task
    template_name = 'detail.html'
    form_class = ToDoForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context['TITLE_SHORT'] = 'Edit'
        context['TITLE_LONG'] = 'Edit a task'
        return context

class ToDoListView(LoginRequiredMixin, PermissionRequiredMixin):
    permission_required = 'Aufgaben.view_aufgabe'
    model = Aufgabe
    template_name = 'liste.html'
    table_class = ToDoTable
