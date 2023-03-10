from django.db import models


class Ram(models.Model):
    gb = models.IntegerField()
    Type = models.CharField(max_length=20)
    def __str__(self):
        return str(self.gb)+' GB '+ str(self.Type) 



class Stokage(models.Model):
    gb = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    def __str__(self):
        return str(self.gb)+' GB '+ str(self.Type)


        
class Processeur(models.Model):
    Name = models.CharField(max_length=20)
    Number = models.CharField(max_length=20)
    vitesse = models.CharField(max_length=20)
    def __str__(self):
        return str(self.Name)+" "+str(self.Number)+" "+ str(self.vitesse)+"GHZ"



class SousModel(models.Model):
    SousmodelName = models.CharField(max_length=20)
    model = models.ForeignKey("Model", on_delete=models.CASCADE , related_name="sousModels")
    def __str__(self):
        return self.SousmodelName


class Model(models.Model):
    modelName = models.CharField(max_length=20)
    def __str__(self):
        return self.modelName


class Pc(models.Model):
    PcName = models.CharField(max_length=20)
    description = models.TextField()
    couleur = models.CharField(max_length=50)
    prix = models.FloatField()
    poid = models.FloatField()
    pouce = models.FloatField()
    tactile = models.BooleanField()
    model = models.ForeignKey("Model", on_delete=models.CASCADE , related_name="Pcs")
    sousmodel = models.ForeignKey("sousModel", on_delete=models.CASCADE , related_name="Pcs" , )
    processeur = models.ForeignKey("Processeur",on_delete=models.CASCADE , related_name="Pcs")
    ram = models.ForeignKey("Ram",on_delete=models.CASCADE , related_name="Pcs")
    stockage = models.ForeignKey("Stokage",on_delete=models.CASCADE , related_name="Pcs" , )

    def __str__(self):
        return str(self.model) + " " + str(self.sousmodel)


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Photos(models.Model):
    pub = models.ForeignKey('Pc', on_delete=models.CASCADE, related_name='photos',blank = True ,null=True)
    photo = models.ImageField(upload_to=upload_to, default='posts/default.jpg')