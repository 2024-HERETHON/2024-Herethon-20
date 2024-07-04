"""
URL configuration for homstPrj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from homst import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homst.urls')),
    path('community/', views.community, name='community'),
    path('community/create/', views.community_create, name='community_create'),
    path('community/<int:pk>/', views.community_detail, name='community_detail'),
    path('community/<int:pk>/update/', views.community_update, name='community_update'),
    path('community/<int:pk>/delete/', views.community_delete, name='community_delete'),
    path('mypage/', views.mypage, name='mypage'),
    path('search/', views.search_results, name='search_results'),
    path('record_detail/<int:record_id>/', views.record_detail, name='record_detail'),
    path('accounts/', include('accounts.urls')),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)