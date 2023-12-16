from rest_framework import serializers
from api.models import User,MyUserManager
# from django.utils.encoding import smart_str ,force_bytes, DjangoUnicodeDecodeError
# from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
from api.models import PersonalInfo,UserExperience,UserEducation




class UserRegistrationSerializer(serializers.ModelSerializer):
    # we are write this becuse we need to confirm password field in our registration request
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['email','name','password','password2','tc']
        extra_kwrags={
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password !=password2:
            raise serializers.ValidationError("password and confirm password does not match")
        return attrs

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class UserExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExperience
        fields = '__all__'


class UserEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEducation
        fields = '__all__'
