from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def Browse(request): # PROFIL
    # model oluştur name, image, pinkodu, user, 
    # oluşturulan profilleri görüntüle
    profil = Profil.objects.filter(user=request.user)
    context = {"profil": profil,}
    if len(profil) < 4:
        if request.method == "POST":
            if request.POST["button"] == "buttonprofil":
                name = request.POST["profil"]
                image = request.FILES["image"]
                try:
                    pinon = request.POST["pinon"]
                except:
                    pinon = False
                pin = request.POST["pin"]
                print("PPPPPPPPPPPPPP:", request.POST)
                
                prcreate = Profil(name=name, image=image, pin=pin, user=request.user, pinon=pinon)
                prcreate.save()
                return redirect('Browse')
    else:
        context.update({'hata':'Maximum Profil sayısına ulaştınız..'})
        
    if request.method == "POST":
        if request.POST["button"] == "buttonpin":
            pin = request.POST["pin"]
            profilid = request.POST["profilid"]
            
            if profil.get(id=profilid).pin == pin:
                return redirect('/netflix/{}/'.format(profilid))
            else:
                context.update({ "hata1": 'Pin Hatalı', "idnumber": profilid})
            
        
    return render(request,'browse.html', context)

def BrowseIndex(request, id): # Profil index
    profil = get_object_or_404(Profil, id=id)
    videos = Video.objects.all()

    
    context = {
        "profil": profil,
        "videos": videos,
    }
    
    return render(request,'browse-index.html',context)

def profilDel(request,id):
    profil = get_object_or_404(Profil, id=id)
    profil.delete()
    return redirect('Browse')