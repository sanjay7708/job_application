from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import SignupSerializer
# Create your views here.

class SignUpView(APIView):
    def post(self,request):
        serliazer=SignupSerializer(request.data)
        if serliazer.is_valid():
            serliazer.save()
            return Response({'message':'User Register Successfully'},status=status.HTTP_201_CREATED)
        return Response(serliazer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username')
        password=data.get('password')

        if not username or not password:
            return Response({'message':'username or password required'},status=status.HTTP_206_PARTIAL_CONTENT)
        user=authenticate(request,username=username,password=password)

        if not user:
            return Response({'message':'invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
        refresh=RefreshToken.for_user(user)
        return Response({'message':'login successfully','access':str(refresh.access_token),'refresh':str(refresh)},status=status.HTTP_200_OK)
        
class LogoutView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        refresh=request.data.get('refresh')
        if not refresh:
            return Response({'message':'refresh token must require'})
        try:
            token=RefreshToken(refresh)
            token.blacklist()
        except:
            pass
        return Response({'message':'logout sucessfully'},status=status.HTTP_205_RESET_CONTENT)
    


