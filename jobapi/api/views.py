from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.serializers import UserRegistrationSerializer,UserLoginSerializer,PersonalInfoSerializer,UserExperienceSerializer,UserEducationSerializer,UserSkillSerializer
from rest_framework.permissions import IsAuthenticated
import json
from django.http import Http404
from django.contrib.auth import authenticate
from api.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from api.models import  PersonalInfo, UserExperience,UserEducation,UserSkill


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
    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,requset,format=None):
         serializer=UserLoginSerializer(data=requset.data)
         if serializer.is_valid(raise_exception=True):
             email = serializer.data.get('email')
             password = serializer.data.get('password') 
             user=authenticate(email=email,password=password) 
             if user is not None:
               token=get_tokens_for_user(user)
               return Response({'token':token,'msg':'login sucssesfull'},status=status.HTTP_200_OK)
             else:
              return Response({'errors':{'non_field_errors':['email or password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
             

class PersonalInfoView(APIView):
    def get(self, request):
        personal_infos = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(personal_infos, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Deserialize the incoming JSON data using the PersonalInfoSerializer
        serializer = PersonalInfoSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():
            # Save the validated data to the database
            serializer.save()

            # Return a success response
            return Response({'msg':'presonal information added sucssesfull'}, status=status.HTTP_201_CREATED)
        else:
            # Return an error response if validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk):
        personal_info = PersonalInfo.objects.get(pk=pk)
        serializer = PersonalInfoSerializer(personal_info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'your personal informatin is updated'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    def delete(self, request, pk):
        # Delete operation: Retrieve the PersonalInfo object by ID and delete it
        personal_info = PersonalInfo.objects.get(pk=pk)
        personal_info.delete()
        return Response({'msg':'presonal information deleted sucssefully s'},status=status.HTTP_204_NO_CONTENT)
    
   

class UserExperienceView(APIView):
    def get(self, request):
        user_experiences = UserExperience.objects.all()
        serializer = UserExperienceSerializer(user_experiences, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'your experience has added sucssefully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    def put(self, request, pk):
        try:
            user_experience = UserExperience.objects.get(pk=pk)
        except UserExperience.DoesNotExist:
            raise Http404

        serializer = UserExperienceSerializer(user_experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your experience has been updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user_experience = UserExperience.objects.get(pk=pk)
        except UserExperience.DoesNotExist:
            raise Http404

        user_experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
class UserEducationView(APIView):
    def get(self, request):
        user_experiences = UserEducation.objects.all()
        serializer = UserEducationSerializer(user_experiences, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = UserEducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'your experience has added sucssefully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

      
    def put(self, request, pk):
        try:
            user_experience = UserEducation.objects.get(pk=pk)
        except UserEducation.DoesNotExist:
            raise Http404

        serializer = UserEducationSerializer(user_experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your education is updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

    def delete(self, request, pk):
        try:
            user_experience = UserEducation.objects.get(pk=pk)
        except UserEducation.DoesNotExist:
            raise Http404

        user_experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
class UserSkillListView(APIView):
    def get(self, request):
        user_skills = UserSkill.objects.all()
        serializer = UserSkillSerializer(user_skills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your skill has been uploded"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

    def put(self, request, pk):
        try:
            user_experience = UserSkill.objects.get(pk=pk)
        except UserSkill.DoesNotExist:
            raise Http404

        serializer = UserSkillSerializer(user_experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"your experience has been updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user_experience = UserSkill.objects.get(pk=pk)
        except UserSkill.DoesNotExist:
            raise Http404