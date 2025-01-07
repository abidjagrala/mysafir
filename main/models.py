from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator  # Add this line
from datetime import datetime

# Create your models here.
class User(AbstractBaseUser):
    pass

class State(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
		

class Year(models.Model):
	hijri = models.CharField(max_length=50)
	english = models.CharField(max_length=50)
	is_current_year = models.BooleanField(default=False, blank=True)
	
	def __str__(self):
		return self.english
	
class Institution(models.Model):
	
	name = models.CharField(max_length=200)
	address = models.TextField()
	state = models.ForeignKey(State, on_delete=models.CASCADE, default=0 )
	#state=models.IntegerField()for Importing data from JSON
	pincode = models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def full_adddres(self):
		return f'{self.address}, {self.state.name} - {self.pincode}'

	def __str__(self):
		return self.name
	
class InstitutionDetails(models.Model):
	HALKA= [
		('A', 'A'),
		('B', 'B'),
		('V', 'V'),
	]
	IJAZAT = (
		('Y', 'Yes'),
		('N', 'No'),
	)
	institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='idetail')
	# institution=models.IntegerField()
	year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name="iyear")
	# year=models.IntegerField()
	moh_name = models.CharField(max_length=200)
	moh_phone = models.CharField(max_length=50)
	safir_name = models.CharField(max_length=200)
	safir_phone = models.CharField(max_length=50)
	safir_aadhar = models.CharField(max_length=50, blank=True, null=True)
	taalim = models.CharField(max_length=100)
	total_students = models.IntegerField(default=0)
	res_students = models.IntegerField(default=0)
	total_teachers = models.IntegerField(default=0)
	donation_day = models.IntegerField(default=0,)
	serial_no = models.IntegerField(default=0)
	halka_code = models.CharField(max_length=1, choices=HALKA)
	ijazat_status = models.CharField(max_length=1, choices=IJAZAT)
	next_donation_year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name="next_donation_year")
	# next_donation_year=models.IntegerField()
	comments = models.TextField(blank=True, null=True)
	safir_photo = models.FileField(upload_to = "media/photos/", blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return self.institution.name
	
	# def clean(self):
	# 	from django.core.exceptions import ValidationError
	# 	if self.res_students > self.total_students:
	# 		raise ValidationError('طعام و قیام  کے طلباء کی تعداد کل طلباء سے کم ہونی چاہئے۔')
		
		
		# def save(self, *args, **kwargs):
		# 	super(InstitutionDetails, self).save(*args, **kwargs)
		
        
        