from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MobileSerializer
from .models import Mobile

class MobileAPIView(ListCreateAPIView):
    serializer_class = MobileSerializer
    queryset = Mobile.objects.all()

class MobileDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MobileSerializer
    queryset = Mobile.objects.all()