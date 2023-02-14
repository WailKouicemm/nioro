from rest_framework import serializers
from .models import *




class HoreurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horeur
        fields = '__all__'

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    photos = PhotosSerializer(many=True)
    class Meta:
        model = Publication
        fields = '__all__'

class MagasinSerializer(serializers.ModelSerializer):
    horeurs = HoreurSerializer(many = True)
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
    magasins = MagasinSerializer(many  = True)
    class Meta:
        model = Categorie
        fields = '__all__'





class JourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jour
        fields = '__all__'





class ServiseNonDispoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiseNonDispo
        fields = '__all__'