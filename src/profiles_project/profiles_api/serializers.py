from rest_framework import serializers
from . import models


class HelloSerializers(serializers.Serializer):
    """Serializers a name field for testing our api"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profiles objects."""

    class Meta:
        model=models.UserProfile
        fields = ('id','name','email','password')
        key_wargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        """Create and return a new User."""

        user = models.UserProfile(
        email=validated_data['email'],
        name = validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
