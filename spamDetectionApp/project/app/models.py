from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File
from io import BytesIO
from django.core.validators import MinValueValidator, MaxValueValidator

class ModelUser(AbstractUser):
    USER_ROLES = [
        ("admin", "admin"),
        ("member", "Member"),
        ("client", "Client"),
    ]
    avatar = models.ImageField(null=True, default="assets/avg/avatar.svg")
    user_role = models.CharField(max_length=20, choices=USER_ROLES)
    REQUIRED_FIELDS = ["email"]


class spamsMessage(models.Model):
    contact = models.CharField(max_length=30)
    message = models.TextField(null=False, default="")
    createat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact_{self.id}"

class Messages(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    adresse = models.CharField(max_length=100)
    senderNumber = models.CharField(max_length=15, null=True, blank=True)
    receiverNumber = models.CharField(max_length=15, null=True, blank=True)
    languages = models.CharField(max_length=20, null=False)
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )
    content = models.TextField(null=False, default="")
    kindmsg = models.BooleanField(null=False)
    age = models.IntegerField(
        null=True, validators=[MinValueValidator(10), MaxValueValidator(120)]
    )
    createat = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("createat",)
        verbose_name_plural = "messages"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=30)
    content = models.TextField(null=False)
    email = models.EmailField(null=False, unique=False)
    createat = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-createat",)
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"Contact_{self.email}"
