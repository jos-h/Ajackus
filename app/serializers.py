from rest_framework.serializers import ModelSerializer
from .models import User, Content


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
