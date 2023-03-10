from django.db import models
from django.contrib.auth.models import User




class Utilisateur(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_de_naissance = models.DateField(auto_now=False, auto_now_add=False)
    profile_picture = models.ImageField(upload_to='profilepics',default='profilepics/default-user.png')
    adress = models.CharField( max_length=50)
    codepostal = models.CharField(max_length=10)
    fav = models.ManyToManyField('Magasin' , blank = True)
    

    def __str__(self):
        return self.user.username 


class Categorie(models.Model):
    categorie_photo = models.ImageField(upload_to='categorie_photo')
    nom = models.CharField(max_length=20)
    vu = models.IntegerField(default = 0)
    def __str__(self):
        return self.nom


class Magasin(models.Model):
    nom = models.CharField(max_length=20, unique= True)
    magasin_photo = models.ImageField(upload_to='magasin_photo',default='magasin_photo/default-mag.png')
    description = models.TextField()
    lien_de_verification = models.CharField(max_length=200,)
    valid = models.BooleanField(default = False)
    lien_facebook = models.CharField( max_length=50)
    lien_instagram = models.CharField( max_length=50)
    lien_snapshat = models.CharField( max_length=50)
    rank = models.FloatField()
    adress = models.CharField( max_length=50)
    latitude = models.FloatField()
    longtitude = models.FloatField()
    parton = models.ForeignKey('Utilisateur', on_delete=models.CASCADE , related_name='ownedMagasins')
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE , related_name='magasins' )

    def __str__(self):
        return self.nom






class Jour(models.Model):
    jour = models.CharField(max_length=50,)
    def __str__(self):
        return self.jour



class Horaire(models.Model):
    heur_debut = models.TimeField( auto_now=False, auto_now_add=False)
    heur_fin = models.TimeField( auto_now=False, auto_now_add=False)
    jour = models.ForeignKey('Jour', on_delete=models.CASCADE )
    magasin = models.ForeignKey('Magasin', on_delete=models.CASCADE , related_name='horeurs')

    def __str__(self):
        return 'horeur :'+str(self.id)


class Publication(models.Model):
    description = models.TextField()
    magasin = models.ForeignKey('Magasin',  on_delete=models.CASCADE , related_name='publications')
    def __str__(self):
        return 'publication n:' +str(self.id) 


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Photos(models.Model):
    pub = models.ForeignKey('Publication', on_delete=models.CASCADE, related_name='photos',blank = True ,null=True)
    photo = models.ImageField(upload_to=upload_to, default='posts/default.jpg')



class Service(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE , related_name='services',)
    prix = models.FloatField()
    rank = models.FloatField(default = 0)
    magasin = models.ForeignKey('Magasin',  on_delete=models.CASCADE , related_name='services')
    def __str__(self):
        return self.nom
    


class ServiceDispo(models.Model):
    jour=models.CharField(max_length=50 )
    heur_debut = models.TimeField(auto_now=False, auto_now_add=False)
    heur_fin = models.TimeField(auto_now=False, auto_now_add=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE , related_name='disponible')
    def __str__(self):
        return str(self.id)

