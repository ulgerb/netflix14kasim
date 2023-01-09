from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profil(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    name = models.CharField(("Profil Adı"), max_length=50)
    image = models.FileField(("Profil Fotoğrafı"), upload_to=None, max_length=100)
    boy = models.BooleanField(("Çocuk"), default=False)
    pinon = models.BooleanField(("Pin Kodu Aktif"), default=False)
    pin = models.CharField(("Pin Kodu"), max_length=50)

    def __str__(self):
        return self.name
    
class Video(models.Model):
    title = models.CharField(("Video Başlığı"), max_length=50)
    text = models.TextField(("Video Konusu"))
    image = models.FileField(("Video"), upload_to='', max_length=100)
    
    def __str__(self):
        return self.title