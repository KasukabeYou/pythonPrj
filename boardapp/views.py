from django.shortcuts import render, redirect
# render →　https://docs.djangoproject.com/ja/3.1/intro/tutorial03/
from django.contrib.auth.models import User
# https://docs.djangoproject.com/ja/3.1/topics/auth/default/
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# サインアップ処理
def signupFunc(request):
    # すべてのレコードを取得(例　<QuerySet [<User: ookubo>, <User: testuser>, <User: boarduser>, <User: bduser>]>)
    # user2 = User.objects.all()
    # user2 = User.objects.get(username='bduser')
    # print(user2.email)
    
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        # 
        try:
            User.objects.get(username=username2)
            return render(request, 'user/signup.html', {'error':'登録済みです'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')
    else:
        print('this is not post method')
        
    # 第1引数として request オブジェクトを、第2引数としてテンプレート名を、第3引数（任意）として辞書を受け取ります。
    return render(request, 'user/signup.html', {'some':'test'})

# https://docs.djangoproject.com/ja/3.1/topics/auth/default/
# ログイン処理
def loginFunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        
        # 認証処理を行う
        user = authenticate(request, username=username2, password=password2)
    
        # ユーザーがいる場合
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    
    return render(request, 'user/login.html')

@login_required
def listFunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'user/list.html', {'object_list':object_list})
    
def logoutFunc(request):
    logout(request)
    return redirect('login')

def detailFunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'user/detail.html', {'object':object})
    
def goodFunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')
    
def readFunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in post.readtext:
        return redirect('list')
    else: 
        post.read = post.read + 1
        post.readtext = post.readtext + ' ' + username
        post.save()
        return redirect('list')

class BoadCreate(CreateView):
    template_name = 'user/create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')