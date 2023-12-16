from django.contrib import admin
from django.urls import path ,include
from api.views import UserRegistrationView
from api.views import  UserLoginView ,PersonalInfoView,UserExperienceView,UserEducationView, UserSkillListView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('presnolinfo/', PersonalInfoView.as_view(),name='presnolinfo'),
    path('presnolinfo/<int:pk>', PersonalInfoView.as_view(),name='presnolinfo'),
    path('userexp/',  UserExperienceView.as_view(),name=' userexp'),
    path('userexp/<int:pk>/',  UserExperienceView.as_view(),name=' userexp'),
    path('useredu/',  UserEducationView.as_view(),name=' useredu'),
    path('useredu/<int:pk>/',  UserEducationView.as_view(),name=' useredu'),
    path('userskill/', UserSkillListView.as_view(), name='user_skill_list'),
    path('userskill/<int:pk>/', UserSkillListView.as_view(), name='user_skill_detail'),
]

    # path('send-reset-password-email/',  SendPasswordResetEmailView.as_view(),name='send-reset-password-email '),
    # path('reset-password/<uid>/<token>/',   UserPasswordResetView.as_view(),name='reset-password '),

    