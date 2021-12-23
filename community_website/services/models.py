from django.db import models

# Create your models here.


class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	address = models.CharField(max_length=120)
	postal_code = models.CharField(max_length=15)
	phone = models.CharField('Phone Number', max_length=30)
	email = models.EmailField('User Email', max_length=120)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Service(models.Model):
	service_id = models.AutoField(primary_key=True)
	name = models.CharField('Service Name', max_length=120)
	service_type = models.CharField('Service Type', max_length=120)
	address = models.CharField(max_length=120)
	postal_code = models.CharField(max_length=15)
	provider = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
	professional = models.BooleanField()
	description = models.TextField(blank=True)
	title_image = models.ImageField(null=True, blank=True, upload_to="images/")

	def __str__(self):
		return self.name


