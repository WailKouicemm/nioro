from rest_framework.response import Response
from .models import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import *
from django.db import IntegrityError
from django.db.models import Q
import json

@api_view(['GET'])
def getAllPc(request):

    q=Pc.objects.all()

    s=PcSerializer(q , many=True)

    return Response(s.data)





@api_view(['GET'])
def getAllPro(request):
    q=Processeur.objects.all()
    s=ProcesseurSerializer(q , many=True)
    return Response(s.data)



@api_view(['GET'])
def filtrer(request):
    

    processeurName = request.GET["processeurName"]
    processeurNum = request.GET["processeurNum"]
    Processeurvitesse = request.GET["Processeurvitesse"]

    StokageGb = request.GET["StokageGb"]
    StokageType = request.GET["StokageType"]

    RamGb = request.GET["RamGb"]
    RamType = request.GET["RamType"]

    modelName = request.GET["modelName"]
    SousmodelName = request.GET["SousmodelName"]

    prixMax = request.GET["prixMax"]
    prixMin = request.GET["prixMin"]

    pouce = request.GET["pouce"]


    pcs = Pc.objects.all()

    if processeurName != "" :
         pcs = pcs.filter(processeur__Name = processeurName)
    if processeurNum != "" :
         pcs = pcs.filter(processeur__Number = processeurNum)
    if Processeurvitesse != "" :
         pcs = pcs.filter(processeur__vitesse = Processeurvitesse)
    

    if StokageGb != "" :
         pcs = pcs.filter(stockage__gb = StokageGb)
    if StokageType != "" :
         pcs = pcs.filter(stockage__Type = StokageType)

    

    if RamGb != "" :
         pcs = pcs.filter(ram__gb = RamGb)
    if RamType != "" :
         pcs = pcs.filter(ram__Type = RamType)



    if modelName != "" :
         pcs = pcs.filter(model__modelName = modelName)
    if SousmodelName != "" :
         pcs = pcs.filter(sousmodel__SousmodelName = SousmodelName)

    if prixMax != "" and prixMin != "":
        pcs = pcs.filter(Q(prix__gte = int(prixMin))&Q(prix__lte = int(prixMax)))
   
        

    
    if pouce != "" :
        p = int(pouce)
        pcs = pcs.filter(pouce = p)

    

    
    s = PcSerializer(pcs , many = True)

    return Response(s.data)






