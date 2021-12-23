from django.contrib import admin
from .models import User
from .models import Service

# Register your models here.

#admin.site.register(User)
#admin.site.register(Service)

# Constructors
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
		list_display = ('first_name', 'last_name', 'user_id', 'phone', 'address')
		ordering = ('first_name', 'last_name',)
		search_fields = ('first_name', 'last_name', 'address')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
		list_display = ('name', 'service_type', 'service_id', 'address', 'professional')
		ordering = ('name', 'service_type',)
		search_fields = ('name', 'service_type', 'address')