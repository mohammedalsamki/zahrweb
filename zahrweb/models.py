import os
import uuid
from sqlite3 import IntegrityError

from django.conf import settings
from django.contrib.auth.models import (  # required to assingn user in borrower
    AbstractBaseUser, AbstractUser, BaseUserManager, Group, Permission,
    PermissionsMixin, User)
from django.core.validators import RegexValidator
## create a model for the user  will contain users info
from django.db import models
from django.urls import \
    reverse  # used to generate URLs by reversing the URL patterns
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# def get_static_path(instance, filename):
#     return os.path.join(settings.STATIC_ROOT, filename)

# Create a new group object
# custom_group = Group(name="Custom Group")
# custom_group.save()
# from django.contrib.auth.models import Group

# group_name = "Custom Group"

# try:
#     # Try to create a new group with this name
#     custom_group = Group.objects.create(name=group_name)
# except IntegrityError:
#     # If the group name already exists, delete it first
#     existing_group = Group.objects.get(name=group_name)
#     existing_group.delete()
#     custom_group = Group.objects.create(name=group_name)

# Add permissions to the custom group
# custom_group.permissions.add(
#     Permission.objects.get(codename="add_customuser"),
#     Permission.objects.get(codename="change_customuser"),
#     Permission.objects.get(codename="delete_customuser"),
# )


# class CustomUser(AbstractUser, PermissionsMixin):
#     # user_permissions = models.ManyToManyField(
#     #     Permission,
#     #     verbose_name=_("user permissions"),
#     #     blank=True,
#     #     related_name="user_permissions_set",
#     #     help_text=_("Specific permissions for this user."),
#     #     through="zahrweb_customuser_user_permissions",
#     # )

#     number_validator = RegexValidator(
#         regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
#         message="Phone number must contain 10 digits",
#     )
#     is_naf = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     mailing_address = models.CharField(max_length=200, blank=True)
#     phoneNumber = models.CharField(
#         max_length=200,
#         blank=True,
#         validators=[number_validator],
#     )
#     RegisterDate = models.DateField(null=True, blank=True)
#     FamilyNumbers = models.IntegerField(
#         help_text="number of family numbers ", default=0
#     )
#     NationalNumber = models.CharField(
#         validators=[number_validator],
#         max_length=10,
#         help_text="Enter a user National Number",
#         null=True,
#         blank=True,
#     )
#     nationality = models.CharField(max_length=50, verbose_name="Nationality")

#     # fields here


# from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser,
#     PermissionsMixin,
#     BaseUserManager,
# )


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["first_name", "last_name"]


# class CustomGroup(models.Model):
#     name = models.CharField(max_length=80, unique=True)
#     description = models.CharField(max_length=255, blank=True)
#     members = models.ManyToManyField(User)

#     class Meta:
#         verbose_name = "Custom Group"
#         verbose_name_plural = "Custom Groups"

#     def __str__(self):
#         return self.name


# class CustomGroup(models.Model):
#     users = models.ManyToManyField(
#         CustomUser, through="CustomMembership", related_name="groups"
#     )


# class CustomMembership(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)
#     date_joined = models.DateField(auto_now_add=True)

# class Meta:
#     db_table = "auth_user"  # <-- you can change me


# Create your models here.

# class User(AbstractUser):
#     age = models.IntegerField(default=0)

# from django.contrib.admin.models import LogEntry
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class CustomLogEntry(LogEntry):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         verbose_name=_("user"),
#         related_name="log_entries",
#     )

#     class Meta:
#         verbose_name = _("log entry")
#         verbose_name_plural = _("log entries")

#     def __str__(self):
#         return str(self.object_repr)


# class UserFiledsMixin:
#     age = models.IntegerField(default=0)


# class CustomUser(AbstractUser, UserFiledsMixin):
#     pass




class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    phoneNumber= models.CharField(max_length=20, blank=True)
    mailing_address = models.CharField(max_length=200, blank=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
# class User(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)
#     number_validator = RegexValidator(
#         regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
#         message="Phone number must contain 10 digits",
#     )
#     # MiddleName = models.CharField(max_length=200, help_text="Enter a user middle name", null=False, blank=False)

#     # MiddleName = models.EmailField(
#     #     max_length=200, help_text="Enter a user middle name", null=False, blank=False
#     # )
#     NationalNumber = models.CharField(
#         validators=[number_validator],
#         max_length=10,
#         help_text="Enter a user National Number",
#         null=False,
#         blank=False,
#     )
#     PhoneNumber = models.CharField(
#         validators=[number_validator],
#         max_length=10,
#         blank=True,
#         help_text="enter phone number",
#     )  # validators should be a list

#     RegisterDate = models.DateField(null=False, blank=False)
#     FamilyNumbers = models.IntegerField(
#         help_text="number of family numbers ", default=0
#     )
#     NAF = models.BooleanField(default=False)
#     REQUIRED_FIELDS = [
#         "email",
#         # "MiddleName ",
#         "NationalNumber",
#         "PhoneNumber",
#     ]
#     USERNAME_FIELD = "username"

#     def __str__(self):
#         return self.NationalNumber


## Create a model for cash donation information


class CashDonation(models.Model):
    Name = models.CharField(max_length=100, help_text="Name of cash donation")
    Email = models.EmailField(
        max_length=100, help_text="Email address of cash donation"
    )
    PhoneNumber = models.IntegerField(help_text="Phone number of cash donation")
    Country = models.CharField(
        max_length=100, help_text="Country of cash donation member"
    )
    Cash = models.IntegerField(help_text="Cash donation")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


## Create a model for in_kind_donation information


class InKindDonation(models.Model):
    Name = models.CharField(max_length=100, help_text="Name of in kind donation ")
    Email = models.EmailField(
        max_length=100, help_text="Email address of in kind donation"
    )
    PhoneNumber = models.IntegerField(help_text="Phone number of in kind donation")
    Country = models.CharField(max_length=100, help_text="Country of in kind donation")
    TypeOfDonation = models.CharField(max_length=100, help_text="Type of donation")
    AmountOfDonation = models.FloatField(max_length=200, help_text="Amount of donation")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


## Create a model for events


class Events(models.Model):
    NameOfEvent = models.CharField(max_length=100, help_text="Name of Event")
    Location = models.CharField(max_length=100, help_text="Location of event")
    DateTimeOFEvent = models.DateTimeField(
        max_length=100, help_text="Date and time of event"
    )
    Description = models.TextField(max_length=400, help_text="Description of event")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.NameOfEvent


##Create a model for news


class News(models.Model):
    Title = models.CharField(max_length=100, help_text="Title of news")
    Image = models.ImageField(upload_to="static/", help_text="Image Poster for news ")
    Details = models.TextField(max_length=30000, help_text="News details")
    date = models.DateField(help_text="Date of news")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Title


# create model that contain image poster for home page
class poster(models.Model):
    image = models.ImageField(help_text="Image Poster for news ")
    details = models.CharField(max_length=100, help_text="News details")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.details


# create a model that contain number of achivment in the year


class Achivment(models.Model):
    Test = models.CharField(default=0, blank=True)
    FamilyAidNumber = models.IntegerField(default=0, help_text="Number of family aids ")
    ProjectsGrants = models.IntegerField(
        default=0, help_text="number of pojects grants"
    )
    EducationBeneficiaries = models.IntegerField(
        default=0, help_text="Number of education beneficiaries "
    )
    HomeProjects = models.IntegerField(default=0, help_text="Number of home projects ")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Test


# create a model that contain currently existing projects info


class ExistingProjects(models.Model):
    # Image = models.ImageField(max_length=400, help_text="project poster image ")
    Image = models.ImageField(help_text="project poster image")

    Name = models.CharField(max_length=100, help_text="Name of project")
    Details = models.TextField(max_length=500, help_text="project details ")
    start_date = models.DateField(help_text="project start date")

    def __str__(self):
        """String for rapresenting the mode object"""
        return self.Name


# Create a model that contains details and about of charitable assosiation info


class About(models.Model):
    About = models.TextField(
        max_length=100000, help_text="About charitable assosiation "
    )
    Image = models.ImageField(help_text="insert about image ", default=0)

    def __str__(self):
        """string for represinting the model object"""

        return str(self.About)


#  Create a model that contains volunteering details
class Volunteer(models.Model):
    # UserName = models.ForeignKey(
    #     CustomUser,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     help_text="Select a user name for the volunteer ",
    # )
    field_of_volunteers = models.CharField(
        max_length=100, help_text="type or field of voulnteer"
    )
    RegisterDate = models.DateField(help_text="Date of registration")


class Idea(models.Model):
    number_validator = RegexValidator(
        regex=r"^\d{10}$",  # Phone number format: +1234567890 or 1234567890
        message="Phone number must contain 10 digits",
    )

    idea = models.TextField(help_text="enter your idea details : ")
    name = models.CharField(max_length=100, help_text="enter your name :")
    PhoneNumber = models.CharField(
        validators=[number_validator],
        max_length=10,
        blank=True,
        help_text="enter phone number",
    )  # validators should be a list

    def __str__(self):
        """string for represinting the model object"""

        return self.name


class number(models.Model):
    year = models.IntegerField(default=0)
    home_project = models.IntegerField(default=0)
    project_grant = models.IntegerField(default=0)
    education_child = models.IntegerField(default=0)
    family_aid = models.IntegerField(default=0)

    def __str__(self):
        """string for represinting the model object"""

        return str(self.year)
