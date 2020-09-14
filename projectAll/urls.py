from django.contrib import admin
from django.urls import path, include
from .views import todoFunc

urlpatterns = [
    # 管理アプリ
    # path(URL, 関数またはクラスなど呼び出す処理)
    path('admin/', admin.site.urls),
    # TODOリストアプリ
    path('todo/', include('todo.urls')),
    #path('a/', todoFunc),
]
