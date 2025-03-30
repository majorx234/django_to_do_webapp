from django.urls import path
# from django.conf.urls import urls

from .views import MainView, ToDoCreateView, ToDoListView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
]
