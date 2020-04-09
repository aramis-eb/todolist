from django.urls import path
from .views import (
    TodoListView,
    TodoCreate,
    TodoDelete,
    TodoEdit,
    TodoReasing,
    TodoDetailView
    )
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='todo_login'),
    path('logout', LogoutView.as_view(), name='todo_logout'),
    path('', TodoListView.as_view(), name='todo_list'),
    path('new/', TodoCreate.as_view(), name='todo_create'),
    path('edit/<pk>', TodoEdit.as_view(), name='todo_update'),
    path('delete/<pk>', TodoDelete.as_view(), name='todo_delete'),
    path('asing/<pk>', TodoReasing.as_view(), name='todo_asing'),
    path('view/<pk>', TodoDetailView.as_view(), name='todo_detail')

]
