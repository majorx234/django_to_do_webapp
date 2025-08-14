from django.urls import path
# from django.conf.urls import urls

from .views import MainView, ToDoCreateView, \
                   ToDoListView, ToDoUpdateView, \
                   ToDoDetailView, ToDoRestDetailView, \
                   ToDoRestListView


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('create/', ToDoCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', ToDoDetailView.as_view(), name='detail'),
    path('rest-detail/<int:pk>/', ToDoRestDetailView.as_view(), name='rest-detail'),
    path('update/<int:pk>/', ToDoUpdateView.as_view(), name='update'),
    path('list/', ToDoListView.as_view(), name='list'),
    path('rest-list/', ToDoRestListView.as_view(), name='rest-list'),
]
