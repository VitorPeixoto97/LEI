from rest_framework import viewsets
from .models import Clube
from .serializers import ClubeSerializer

class ClubeViewSet(viewsets.ModelViewSet):
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer