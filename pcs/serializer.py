
from rest_framework import serializers
from .models import *






class PcSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Pc
        fields = '__all__'

class SousModelSerializer(serializers.ModelSerializer):
    Pcs = PcSerializerSimple(many = True)
    class Meta:
        model = SousModel
        fields = '__all__'

class SousModelSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = SousModel
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    Pcs = PcSerializerSimple(many = True)
    SousModel = SousModelSerializer()
    class Meta:
        model = Model
        fields = '__all__'

class ModelSerializerSimple(serializers.ModelSerializer):
    SousModel = SousModelSerializer(many = True)
    class Meta:
        model = Model
        fields = '__all__'


class ProcesseurSerializer(serializers.ModelSerializer):
    Pcs = PcSerializerSimple(many = True)
    class Meta:
        model = Processeur
        fields = '__all__'

class ProcesseurSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Processeur
        fields = '__all__'



class RamSerializer(serializers.ModelSerializer):
    Pcs = PcSerializerSimple(many = True)
    class Meta:
        model = Ram
        fields = '__all__'

class RamSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'


class StokageSerializer(serializers.ModelSerializer):
    pcs = PcSerializerSimple(many = True)
    class Meta:
        model = Stokage
        fields = '__all__'

class StokageSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Stokage
        fields = '__all__'


class PcSerializer(serializers.ModelSerializer):
    sousmodel = SousModelSerializerSimple()
    processeur = ProcesseurSerializerSimple()
    ram = RamSerializerSimple()
    stockage = StokageSerializerSimple()
    class Meta:
        model = Pc
        fields = '__all__'
