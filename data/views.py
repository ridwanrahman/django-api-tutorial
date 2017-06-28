from .serializers import dataSerializer
from .models import data
from rest_framework import generics
# Create your views here.

class dataList(generics.ListCreateAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerializer

class dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerializer