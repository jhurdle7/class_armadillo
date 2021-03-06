
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('todo/', include('todo.urls')),
    path('blogapp/', include('blogapp.urls')),
    path('demo/', include('demo.urls')),
]
