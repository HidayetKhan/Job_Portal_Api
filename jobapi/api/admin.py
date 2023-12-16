from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import User,PersonalInfo,UserExperience,UserEducation,UserSkill
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["id","email", "name", "tc","is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(User, UserModelAdmin)
admin.site.register(PersonalInfo)
admin.site.register(UserExperience)
admin.site.register(UserEducation)
admin.site.register(UserSkill)
