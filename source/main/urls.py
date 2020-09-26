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
from webapp.views.review_views import ReviewView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', IndexView.as_view(), name='index'),
    path('product/', include([
            path('<int:pk>/', include([
                path('', ProductView.as_view(), name='product_view'),
                path('update/', ProductUpdateView.as_view(), name='product_update'),
                path('delete/', ProductDeleteView.as_view(), name='product_delete'),
    ])),
    path('review/', include([
        path('<int:pk>/', include([
            path('', ReviewView.as_view(), name='review_view'),
            path('', ReviewCreateView.as_view(), name='review_create'),
            path('', ReviewUpdateView.as_view(), name='review_update'),
            path('', ReviewDeleteView.as_view(), name='review_delete'),

            ]))
        ]))
    ]))
]
