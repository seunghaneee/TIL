from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 회원가입
from django.contrib.auth.forms import UserCreationForm
# CustomUserCreationForm()으로 대체하기
from .forms import CustomUserCreationForm, CustomUserChangeForm
# 비밀번호 변경 폼
from django.contrib.auth.forms import PasswordChangeForm
# 비밀번호 변경 후에도 로그인 유지 될 수 있도록 세션 무효화 방지
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 곧바로 로그인 진행
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    request.user.delete()
    # 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶은 경우
    auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)