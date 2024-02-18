from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='index'),
    path('<str:url>/', views.url_view),
    path('short/<str:short>/', views.short_view, name='short'),
    path('<str:short>/stats', views.short_stats),
]
