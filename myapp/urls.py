from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('contact/', views.contact),
    path('test_app/', include("test_app.urls"))
]
