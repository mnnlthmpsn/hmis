import uuid
from django.urls import reverse
from django.db import models
from .managers import AuthManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Staff(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    staff_ID = models.CharField(verbose_name='staff ID', max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AuthManager()

    USERNAME_FIELD = 'staff_ID'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_absolute_url(self):
        return reverse('administrator:update_staff', args=[self.id])

# Roles
class Role(models.Model):
    name = models.CharField(max_length=20, default='Not Assigned', unique=True, 
    null=False, blank=False)

    def __str__(self):
        return self.name

# Profile for staff
class Profile(models.Model):
    staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name='Firstname', max_length=100)
    lastname = models.CharField(verbose_name='Lastname', max_length=100)
    telephone = models.CharField(verbose_name='Telephone Number', max_length=13)
    date_of_birth = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.staff.staff_ID}"

    def full_name(self):
        return f"{self.firstname} {self.lastname}"