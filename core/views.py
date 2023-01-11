from rest_framework import viewsets
from .models import User, Profile
from .serializers import UserProfileSerializer, Profile, ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer