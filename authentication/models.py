from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
	"""
	Custom user model manager where email is the unique identifiers
	for authentication instead of usernames.
	"""
	def create_user(self, mobile_no, password, **extra_fields):
		"""
		Create and save a User with the given email and password.
		"""
		if not mobile_no:
			raise ValueError(_('The Mobile number must be set'))
		user = self.model(mobile_no=mobile_no, **extra_fields)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, mobile_no, password, **extra_fields):
		"""
		Create and save a SuperUser with the given email and password.
		"""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError(_('Superuser must have is_staff=True.'))
		if extra_fields.get('is_superuser') is not True:
			raise ValueError(_('Superuser must have is_superuser=True.'))
		return self.create_user(mobile_no, password, **extra_fields)


class User(AbstractBaseUser):
	username = None
	sponsor = models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
	mobile_no = models.CharField(max_length=10, unique=True)
	email = models.EmailField(verbose_name="email", max_length=60, unique=False,blank=True,null=True)
	first_name = models.CharField(max_length=30, unique=False,blank=True,null=True)
	last_name = models.CharField(max_length=30, unique=False,blank=True,null=True)
	address = models.CharField(max_length=200,blank=True,null=True)
	dob = models.DateTimeField(verbose_name='date of birth', null=True, blank=True)
	state = models.CharField(max_length=100,blank=True,null=True)
	city = models.CharField(max_length=50,blank=True,null=True)
	zip_code = models.CharField(max_length=6,blank=True,null=True)
	profile_pic = models.ImageField(upload_to="profile_pics",null=True,blank=True)
	password1 = models.CharField(max_length=30,null=True,blank=True)
	username = models.CharField(max_length=30, unique=True)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	date_active	= models.DateTimeField(verbose_name='date active',null=True,blank=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_active1 = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'mobile_no'
	REQUIRED_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.mobile_no

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True