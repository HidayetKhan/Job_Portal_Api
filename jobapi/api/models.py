from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.core.exceptions import ValidationError


#custom user manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,verbose_name='Email',unique=True)
    name = models.CharField(max_length=255)
    tc = models.BooleanField()
    # profile_pic = models.ImageField(upload_to="media", default="profile_pic.jpg")
    # back_pic = models.ImageField(upload_to="media", default="back_profile.webp")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','tc']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # simplest possible answer: Yes always
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'? "
        #simplest possible answer:Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a number of staff?"
        # simplest possible answer: All admins are staff
        return self.is_admin
    

class PersonalInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    location=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} "
    
    def validate_phone_number(self):
        if self.phone_number:
            # Check if the phone number contains only digits
            if not self.phone_number.isdigit():
                raise ValidationError("Phone number must contain only digits.")

            # Check if the length of the phone number is within a valid range
            min_length = 8
            max_length = 15
            if not min_length <= len(self.phone_number) <= max_length:
                raise ValidationError(f"Phone number must be between {min_length} and {max_length} characters.")
        else:
            # Handle the case where phone_number is None or an empty string
            raise ValidationError("Phone number is required.")
        

class UserExperience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    role=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    year_of_experience = models.PositiveIntegerField()
    current_ctc = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" Experience at {self.company}"
    
    def clean(self):
        # Add custom validation logic
        if self.year_of_experience < 0:
            raise ValidationError("Year of experience must be a non-negative integer.")

class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    start_year = models.DateField()  # Removed extra 'models'
    end_year = models.DateField()    # Removed extra 'models'
    grade = models.IntegerField()

    def clean(self):
        if self.start_year > self.end_year:
            raise ValidationError("Start year must be before end year.")
        

    def is_honors_student(self):
        return self.grade >= 90    
    

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
