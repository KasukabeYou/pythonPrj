#from django.contrib import admin
from django.urls import path, include
from .views import todo, TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete

urlpatterns = [
    path('todosample/', todo),
    # TODOリスト一覧
    path('list/', TodoList.as_view(), name='todolist'),
    # TODO詳細
    path('detail/<int:pk>', TodoDetail.as_view(), name='tododetail'),
    # TODO登録
    path('create/', TodoCreate.as_view(), name='todocreate'),
    # TODO編集
    path('update/<int:pk>', TodoUpdate.as_view(), name='todoupdate'),
    # TODO削除
    path('delete/<int:pk>', TodoDelete.as_view(), name='tododelete'),
]
