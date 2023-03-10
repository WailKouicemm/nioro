from rest_framework import serializers
from .models import *




class HoraireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horaire
        fields = '__all__'

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'


class ServiseNonDispoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDispo
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    disponible =  ServiseNonDispoSerializer(many = True)
    class Meta:
        model = Service
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    photos = PhotosSerializer(many=True)
    class Meta:
        model = Publication
        fields = '__all__'
class ServiseNonDispoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDispo
        fields = '__all__'



class MagasinSerializer(serializers.ModelSerializer):
    #Horaire = HoraireSerializer(many = True)
    publications = PublicationSerializer(many = True)
    services = ServiceSerializer(many = True)
    class Meta:
        model = Magasin
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    ownedMagasins=MagasinSerializer(many = True)
    class Meta:
        model = Utilisateur
        fields = '__all__'


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'





class JourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jour
        fields = '__all__'




