from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer, CustomUserSerializer, PackageSerializer, CourierSerializer
from .models import Package, Courier

# Create your views here.
class ObtainTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PackageView(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = PackageSerializer
    queryset = Package.objects.all()

class CourierView(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()