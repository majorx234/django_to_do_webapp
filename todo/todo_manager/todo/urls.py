from django.urls import path
# from django.conf.urls import urls

from .views import MainView, ToDoCreateView, ToDoListView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('todo/create/', ToDoCreateView.as_view(), name='create'),
    path('todo/list/', ToDoListView.as_view(), name='list'),
]
