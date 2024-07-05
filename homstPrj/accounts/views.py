from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat']

        if password != repeat_password:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        if len(password) < 8:
            messages.error(request, '비밀번호는 8자리 이상이어야 합니다.')

        if not User.objects.filter(username=email).exists() and password == repeat_password and len(password) >= 8: #중복가입시
            new_user = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, '회원가입 성공')
            return redirect('accounts:login')
    
    return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # 사용자가 존재하지 않는 경우, 회원가입 페이지로 이동
            messages.error(request, '해당 아이디로 가입된 계정이 없습니다. 회원가입을 진행해주세요.')
            return redirect('accounts:signup') 
        

        user = authenticate(request, username=username, password = password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('main') #로그인성공->main
        else: 
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."  # 에러 메시지 설정
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth_logout(request)
    print('로그아웃 성공')
    return redirect('main')


@login_required
def mypage(request):
    return render(request, 'mypage.html')

@login_required
def community(request):
    return render(request, 'mypage.html')