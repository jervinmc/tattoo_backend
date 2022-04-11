from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Tattoo
from .serializers import TattooSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class TattooView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Tattoo.objects.all()
    serializer_class=TattooSerializer



class TattooUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            tattoo = Tattoo.objects.filter(user_id=user_id)
            serializers = TattooSerializer(tattoo,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
