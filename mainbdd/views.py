from rest_framework.response import Response
from .models import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import *

@api_view(['GET'])
def getAllMagasins(request):

    q=Service.objects.all()

    s=ServiceSerializer(q, many=True)

    return Response(s.data)