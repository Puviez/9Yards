from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid

from .managers import CustomUserManager

"""
Create a Custom User Model using email as a login name returning email
"""

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('Email'), unique=True)
    fullname = models.CharField(_('Name'), max_length=40)
    address = models.TextField(_('Address'), blank=True)

	# Choices
    USER_TYPE = (
		('CU', 'Customer'),
		('ST', 'Staff')
	)
    user_type = models.CharField('User Type', max_length=2, choices=USER_TYPE, default='CU', null=False, blank=True)
    is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active.'
			'Unselect this instead of deleting accounts.'
		),
	)
    is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_(
			'Designates whether the user can log into this admin site.'
		),
	)
	
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
	
    objects = CustomUserManager()
	
    class Meta:
        verbose_name = "Custom user"
        verbose_name_plural = "Custom users"
        
    def __str__(self):
    	return self.email
	
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
		# Simplest possible answer: Yes, always
        return True
	
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
		# Simplest possible answer: Yes, always
        return True

class Package(models.Model):
    description = models.TextField()
    # Choices
    PKG_STATUS = (
		('U', 'Unassigned'),
		('A', 'Assigned'),
        ('P', 'Picked Up'),
        ('D', 'Delivered')
	)
    status = models.CharField('Status', max_length=1, choices=PKG_STATUS, default='U', null=False)
    sender = models.ForeignKey(CustomUser, related_name='package_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,related_name='package_receiver', on_delete=models.CASCADE)

    def _str_(self):
        return self.description

class Courier(models.Model):
    name = models.CharField(max_length=120)
    C_STATUS = (
		('B', 'Busy'),
		('A', 'Available')
	)
    status = models.CharField('User Type', max_length=1, choices=C_STATUS, default='A', null=False)
    package = models.ForeignKey(Package, on_delete=models.PROTECT)

    def _str_(self):
        return self.name


