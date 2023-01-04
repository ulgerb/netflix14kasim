from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from appMy.models import Profil

def accountUser(request,id):
    profil = get_object_or_404(Profil,id=id)

    context = {
        "profil": profil,
    }
    return render(request, 'user/hesap.html',context)

# Kaydol
def registerUser(request):

    if request.method=="POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1==password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username,password=password1,
                                                    email=email,first_name=name,last_name=surname)
                    user.save()
                    return redirect('loginUser')
                else:
                    hata = 'Bu mail zaten başkası tarafından kullanılıyor!'
                    return render(request,'user/register.html', {"hata":hata})
            else:
                hata = 'Bu Kullanıcı adı zaten başkası tarafından kullanılıyor!'
                return render(request, 'user/register.html', {"hata": hata})
        else:
            hata = 'Şifreler aynı değil!'
            return render(request, 'user/register.html', {"hata": hata})
                
    return render(request,'user/register.html')
# Giriş Yap
def loginUser(request):
    # Email kontrol
    def mailKontrol(username):
        et = username.find('@')
        com = username.find('.com')
        if et != -1 and com != -1:
            return True
        else:
            return False
    # Giriş
    if request.method=="POST":
        username = request.POST["username"] # berkay@asd
        password = request.POST["password"]

        if mailKontrol(username):
            username1 = get_object_or_404(User,email=username)
            username = username1.username
            

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Browse')
        else:
            hata = 'Kullanıcı adı veya şifre yanlış!'
            return render(request,'user/login.html',{"hata":hata})
        
    return render(request,'user/login.html')
# Çıkış Yap
def logoutUser(request):
    logout(request)
    return redirect('index')


