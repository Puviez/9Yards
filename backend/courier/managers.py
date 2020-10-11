from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class UserProfileManager(models.Manager):
	pass


class CustomUserManager(BaseUserManager):
    """
		Custom user model manager where email is the unique identifiers
		for authentication instead of usernames. m.
	"""
    
    def create_user(self, email, fullname, password, **extra_fields):
        """
		Create and save a User with the given email and password.
		"""
        if not email:
            raise ValueError(_('The Email must be set'))
        if not fullname:
            raise ValueError(_('Name must be set'))
        email = self.normalize_email(email)
        user = self.model(
			email = email,
			fullname = fullname,
			**extra_fields,
		)
        user.user_type = "CU"
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff(self, email, fullname, password, **extra_fields):
        """
		Create and save a User with the given email and password.
		"""
        if not email:
            raise ValueError(_('The Email must be set'))
        if not fullname:
            raise ValueError(_('Name must be set'))
        email = self.normalize_email(email)
        user = self.model(
			email = email,
			fullname = fullname,
			**extra_fields,
		)
        user.user_type = "ST"
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, fullname, password, **extra_fields):
        """
		Create and save a SuperUser with the given email and password.
		"""
        user = self.create_user(
			email,
			fullname=fullname,
			password=password,
		)
        user.user_type = "ST"
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user