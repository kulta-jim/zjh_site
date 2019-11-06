"""zjh_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = '[blog]'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-list/', views.BlogView.as_view(), name='blog-list'),
    path('blog-base-category/<int:base_category_id>/', views.BaseCategoryView.as_view(), name='blog-base-category'),
    path('blog-category/<int:category_id>/', views.CategoryView.as_view(), name='blog-category'),
    path('blog-tag/<int:tag_id>/', views.TagView.as_view(), name='blog-tag'),
    path('blog-detail/<int:blog_id>/', views.BlogDetail.as_view(), name='blog-detail', ),
    path('filter/', views.FilterView.as_view(), name='filter'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
