from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name='blog_api'
urlpatterns = [

    path('<slug:pk>/', views.singleBlog, name='blog'),
    path('', views.allBlog, name='blogs'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
