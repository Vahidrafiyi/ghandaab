from drf_writable_nested import serializers as nested_serializers
from rest_framework import serializers
from .models import User, Profile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']


class ProfileSerializer(nested_serializers.WritableNestedModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = Profile
        fields = [
            'id', 'user','image', 'phone',
            'biography', 'gender'
        ]