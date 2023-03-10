from rest_framework.response import Response
from .models import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import *
from django.db import IntegrityError
from django.db.models import Q


@api_view(['GET'])
def getAllMagasins(request):

    #u = Utilisateur.objects.all()
    q=Utilisateur.objects.get(id=3)

    s=UtilisateurSerializer(q)

    return Response(s.data)




@api_view(['GET'])
def getUserDetails(request, id):
    user = Utilisateur.objects.get(id = id)
    serializer = UtilisateurSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def getTopCategories(request):
    categories = Categorie.objects.order_by('-vu')[:10]
    serializer = CategorieSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAllCategories(request):
    categories = Categorie.objects.all()
    serializer = CategorieSerializer(categories, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def getMagasinsEnTandance(request):
    magasins = Magasin.objects.order_by('-rank')[:10]
    serializer = MagasinSerializer(magasins, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getFavoris(request,id):
    user = Utilisateur.objects.get(id=id)
    magasins = user.fav
    serializer = MagasinSerializer(magasins, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCategorieMagasins(request , id):
    categorie = Categorie.objects.get(id = id)
    categorie.vu = categorie.vu + 1 
    categorie.save()
    serializer = MagasinSerializer(categorie.magasins, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMagasinDetail(request , id):
    magasin = Magasin.objects.get(id = id)
    serializer = MagasinSerializer(magasin)
    return Response(serializer.data)

@api_view(['GET'])
def getPublicationDetails(request , id):
    pub = Publication.objects.get(id = id)
    serializer = PublicationSerializer(pub)
    return Response(serializer.data)




@api_view(['POST'])
def user(request):
    user = request.user()
    return Response(user)






@api_view(['POST'])
def postPublication(request , id):

    files = request.FILES.getlist('uploaded_photos')
    if files:
        request.data.pop('uploaded_photos')

    magasin = Magasin.objects.get(id = id)


    publication = Publication.objects.create(
            description = request.data.get("description"),
            magasin =magasin,
    )
    
    publication.save()

    for file in files:
                p = Photos.objects.create(pub=publication, photo=file)
                p.save()


    serializer = PublicationSerializer(publication)

    return Response(serializer.data)



@api_view(['PUT'])
def ModifierMagasin(request , id):
    Magasin.objects.filter(id = id).update(
        nom = request.data["nom"],
        description = request.data["description"],
        adress = request.data["adress"],
        lien_facebook = request.data["nom"],
        )
    magasin = Magasin.objects.get(id = id)
    serializer = MagasinSerializer(magasin)
    return Response(serializer.data)









@api_view(['POST'])
def postMagasin(request,id):
            
    user = Utilisateur.objects.get(id = id)
    categorie = Categorie.objects.get(nom = request.data['categorie'])
    try: 
        magasin = Magasin.objects.create(
        nom = request.data.get('nom'),
        magasin_photo = request.data.get('magasin_photo'),
        description = request.data['description'],
        lien_instagram = request.data['lien_instagram'],
        lien_facebook = request.data['lien_facebook'],
        lien_snapshat = request.data['lien_snapshat'],
        rank = 0 ,
        adress = request.data['adress'],
        latitude = request.data['latitude'],
        longtitude = request.data['longtitude'],
        parton = user,
        categorie = categorie,
        lien_de_verification = request.data['lien_de_verification'],
        )   
        magasin.save()
        ser = MagasinSerializer(magasin)
        return Response(ser.data)
    except IntegrityError :
            return Response({'detail':'change the name'})


@api_view(['POST'])
def postHoreur(request,id):
    mag = Magasin.objects.get(id=id)
    req = request.data
    for i in req :
        jour = Jour.objects.get(jour=i["jour"])
        h = Horaire.objects.create(
            heur_debut= i["heur_debut"],
            heur_fin = i["heur_fin"],
            magasin = mag,
            jour = jour
        )
    return Response('created')





@api_view(['GET'])
def filtrer(request,prix_max,prix_min,rank_min,rank_max,categorie):

    if categorie == 0 : 
        service = Service.objects.filter(Q(prix__gte=prix_min) & Q(prix__lte=prix_max) & Q(rank__gte=rank_min) & Q(rank__lte=rank_max))
    else : 
        service = Service.objects.filter(Q(prix__gte=prix_min) & Q(prix__lte=prix_max) & Q(rank__gte=rank_min) & Q(rank__lte=rank_max)& Q(categorie=categorie))
    ser = ServiceSerializer(service, many = True)
    lis = []
    dispo = ServiceDispo.objects.filter(Q(heur_debut__gte="6:00:00") & Q(heur_fin__lte="22:45:49")&Q(jour = "mardi")).values()
    for d in dispo :
        service = Service.objects.get(id= d["service_id"])
        s = ServiceSerializer(service)
        lis.append(s.data)
    
    return Response(ser.data and lis)








@api_view(['GET'])
def getALlServices(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many = True)
    return Response(serializer.data)




