from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from .models import Staff, Profile, Role

# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = ('email', 'staff_ID')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password1:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('email', 'password', 'staff_ID', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'staff_ID', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    fieldsets =(
        (None, {'fields': ('staff_ID', 'email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('staff_ID', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'staff_ID')
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Staff, UserAdmin)
admin.site.unregister(Group)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'firstname', 'lastname', 'telephone', 'role')
    list_filter = ('role',)
    search_fields = ('staff', 'firstname', 'lastname')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)