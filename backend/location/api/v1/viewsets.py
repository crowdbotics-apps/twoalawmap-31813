from rest_framework import authentication
from location.models import User_location
from .serializers import User_locationSerializer
from rest_framework import viewsets


class User_locationViewSet(viewsets.ModelViewSet):
    serializer_class = User_locationSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = User_location.objects.all()
