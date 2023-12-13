from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate
from api.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)

    return {
         'refresh':str(refresh),
         'access':str(refresh.access_token),

    }
# Create your views here.
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            #token=get_tokens_for_user(user)
            return Response({'msg':'registration sucssesfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    