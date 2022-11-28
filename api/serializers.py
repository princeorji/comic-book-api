from rest_framework import serializers

from users.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ArtistSerializer(serializers.ModelSerializer):
    artist = UserSerializer()

    class Meta:
        model = Artist
        exclude = ['id',] 

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__' 

class IssueSerializer(serializers.ModelSerializer):
    series_id = SeriesSerializer()

    class Meta:
        model = Issue
        fields = '__all__' 