from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UserTable(AbstractUser):
    date_of_birth = models.DateField(null=True,blank=True)
    GENDER_CHOICES = [
        ('Male','male'),
        ('Female','female'),
        ('Other','other')
    ]
    gender = models.CharField(max_length=15,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12,unique=True)
    full_address = models.TextField()
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=15,choices=ROLE_CHOICES,default = 'student')
    profile_pic = models.ImageField(upload_to='profile_pics',null=True,blank=True)

    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions', blank=True)
    def __str__(self):
        return f"{self.username} - {self.role}"