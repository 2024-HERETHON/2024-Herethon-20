from django.urls import path
from accounts import views

app_name = "accounts" #namespace 가 accounts 라는 이름을 가졌음을 명시

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), #추가
    path('logout/', views.logout, name='logout'),
]