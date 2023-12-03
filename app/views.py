from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
# Create your views here.

class Productdata(APIView):
    def get(self,request,pid):
        PO=Product.objects.all()
        CJD=ProductModelSerializer(PO,many=True)
        return Response(CJD.data)
    def post(self,request,pid):
        CJD=request.data
        PD=ProductModelSerializer(data=CJD)
        if PD.is_valid():
            PD.save()
            return Response({'message':'data is inserted'})
        else:
            return Response({'message':'data is not inserted'})
        
    def put(self,request,pid):
        CJD=request.data
        PO=Product.objects.get(pid=CJD['pid'])
        PD=ProductModelSerializer(PO,data=CJD)
        if PD.is_valid():
            PD.save()
            return Response({'message':'data is updated'})
        else:
            return Response({'message':'data is not updated'})
    def patch(self,request,pid):
        CJD=request.data
        PO=Product.objects.get(pid=CJD['pid'])
        PD=ProductModelSerializer(PO,data=CJD,partial=True)
        if PD.is_valid():
            PD.save()
            return Response({'message':'data is updated'})
        else:
            return Response({'message':'data is not updated'})
        
   
    def delete(self,request,pid):
        PO=Product.objects.get(pid=pid)
        PO.delete()
        return Response({'message':'delete the instanse'})
    
    

