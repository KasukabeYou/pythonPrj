from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TodoModel
from django.urls import reverse_lazy

# サンプル
def todo(req):
    return HttpResponse('')

# 表示用
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

# 詳細
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
    
# 作成
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = {'title', 'memo', 'priority', 'duedate'}
    success_url = reverse_lazy('list')
    
# 更新
class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = {'title', 'memo', 'priority', 'duedate'}
    success_url = reverse_lazy('list')

# 削除
class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')