from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser, Package, Courier

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['fullname'] = user.fullname
        token['address'] = user.address
        token['usertype'] = user.user_type
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    fullname = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'fullname', 'password', 'address', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data) 
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ('description', 'status', 'sender', 'receiver')

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('name', 'status', 'package')