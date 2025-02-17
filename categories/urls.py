from django.urls import path
from . import views
from .views import CategoryViewSet

urlpatterns = [
    path("", views.CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create',

    })),
    path("<int:pk>", views.CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),
]