from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('community/', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),
    path('search/', views.search_results, name='search_results'),
    path('record_detail/<int:record_id>/', views.record_detail, name='record_detail'),
    path('community/create/', views.community_create, name='community_create'),
    path('community/<int:pk>/', views.community_detail, name='community_detail'),
    path('community/<int:pk>/update/', views.community_update, name='community_update'),
    path('community/<int:pk>/delete/', views.community_delete, name='community_delete'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)