from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.views.generic.detail import DetailView
from .models import Todo
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class TodoListView(PaginationMixin, LoginRequiredMixin, ListView):
    paginate_by = 3

    def get_queryset(self):
        return Todo.objects.filter(assigned_user=self.request.user)


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    fields = [
        'tittle', 'description', 'done', 'priority'
        ]
    success_url = reverse_lazy('todo_list')

    def form_valid(self, form):
        form.instance.assigned_user = self.request.user
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo_detail', args=(self.object.id,))


class TodoEdit(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = [
        'tittle', 'description', 'done', 'priority'
        ]
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('todo_list')

    def get_success_url(self):
        return reverse('todo_detail', args=(self.object.id,))

    def get_object(self):
        todo = super().get_object().assigned_user.id
        if todo != self.request.user.id: 
            raise PermissionDenied
        else:
            return super().get_object()


class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

    def get_object(self):
        todo = super().get_object().assigned_user.id
        if todo != self.request.user.id:
            raise PermissionDenied
        else:
            return super().get_object()


class TodoReasing(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ['assigned_user']
    success_url = reverse_lazy('todo_list')

    def get_object(self):
        todo = super().get_object().assigned_user.id
        if todo != self.request.user.id:
            raise PermissionDenied
        else:
            return super().get_object()


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    success_url = reverse_lazy('todo_list')

    def get_object(self):
        todo = super().get_object().assigned_user.id
        if todo != self.request.user.id:
            raise PermissionDenied
        else:
            return super().get_object()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
