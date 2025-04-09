from django.urls import path
# from django.conf.urls import urls

from .views import MainView, ToDoCreateView, \
                   ToDoListView, ToDoUpdateView, \
                   ToDoDetailView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', ToDoCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ToDoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ToDoUpdateView.as_view(), name='update'),
    path('list/', ToDoListView.as_view(), name='list'),
]
