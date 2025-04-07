from django.urls import path
# from django.conf.urls import urls

from .views import MainView, ToDoCreateView, ToDoListView, ToDoUpdateView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', ToDoCreateView.as_view(), name='create'),
    path('update/', ToDoUpdateView.as_view(), name='update'),
    path('list/', ToDoListView.as_view(), name='list'),
]
