from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 管理アプリ
    # path(URL, 関数またはクラスなど呼び出す処理)
    path('admin/', admin.site.urls),
    # TODOリストアプリ
    path('todo/', include('todo.urls')),
    # 簡易SNS
    path('board/', include('boardapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
