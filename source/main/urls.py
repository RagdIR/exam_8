"""main URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from webapp.views.product_views import IndexView, ProductView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', IndexView.as_view(), name='index'),
    path('product/', include([
            path('<int:pk>/', include([
                path('', ProductView.as_view(), name='product_view'),
                path('update/', ProductUpdateView.as_view(), name='product_update'),
                path('delete/', ProductDeleteView.as_view(), name='product_delete'),
                path('reviews/add/', ProductReviewCreateView.as_view(),
                 name='article_comment_add')
]))]))]
