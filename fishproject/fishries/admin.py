from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *
import time, datetime
from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from .forms import *
# Register your models here.
admin.site.site_header = 'ગુજરાત મત્સ્યઉધોગ'                    # default: "Django Administration"
admin.site.index_title = 'ગુજરાત મત્સ્યઉધોગ'  



class BoatAdmin(admin.ModelAdmin):
    list_display = ['boat_name','boat_number','lisence_number','port_name','boat_material','dimension_length','dimension_breadth','dimension_depth','engine_name','engine_number','engine_manufacture_date','engine_horsepower','owner_details','created_by','updated_by','created_At','updated_At']
    fieldsets = [
        (None,{'fields':('boat_name','boat_number','lisence_number','port_name','boat_material','dimension_length','dimension_breadth','dimension_depth','engine_name','engine_number','engine_manufacture_date','engine_horsepower','owner_details')}),
        ]
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_at', None) is None:
            obj.created_by = request.user
            obj.created_at = int(time.time())
        obj.updated_by = request.user
        obj.updated_at = int(time.time())
        obj.save()

    def created_At(self, obj):
        query = Boat_Details.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.updated_at)
        return f"{date:%d-%b-%Y}"
    
    def updated_At(self, obj):
        query = Boat_Details.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.updated_at)
        return f"{date:%d-%b-%Y}"



class TokenAdmin(admin.ModelAdmin):
    
    list_display = ['fishing_lisence_number','location_of_operation','date_depature','tentative_date','quantity_water','quantity_fuel','owner','number_of_crew']
    fieldsets = [
        (None,{'fields':('fishing_lisence_number', 'location_of_operation','date_depature','tentative_date','quantity_water','quantity_fuel','owner','number_of_crew')}),
    ]
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_at', None) is None:
            obj.created_by = request.user
            obj.created_at = int(time.time())
        obj.updated_by = request.user
        obj.updated_at = int(time.time())
        obj.save()

    def created_At(self, obj):
        query = Token_Book.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.updated_at)
        return f"{date:%d-%b-%Y}"
    
    def updated_At(self, obj):
        query = Token_Book.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.updated_at)
        return f"{date:%d-%b-%Y}"

class AdminTokenAdmin(admin.ModelAdmin):  
    pass

class CrewAdmin(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','aadhar_number','phone_number','alternate_number','email','address','created_by','updated_by','created_At','updated_At']
    fieldsets = [
        (None, {'fields':('first_name','middle_name','last_name','aadhar_number','phone_number','alternate_number','email','address')}),
        ]
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_at', None) is None:
            obj.created_by = request.user
            obj.created_at = int(time.time())
        obj.updated_by = request.user
        obj.updated_at = int(time.time())
        obj.save()

    def created_At(self, obj):
        query = Crew.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.created_at)
        return f"{date:%d-%b-%Y}"
    
    def updated_At(self, obj):
        query = Crew.objects.filter(id=obj.pk).get()
        date = datetime.datetime.fromtimestamp(query.updated_at)
        return f"{date:%d-%b-%Y}"

class BoatdetailAdmin(admin.ModelAdmin):
    list_display = ['fishing_lisence_number','token_number','location_of_operation','date_depature','tentative_date','quantity_fuel','owner','number_of_crew']

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','phone_number','alternate_number','address','email','aadhar_number','username', 'password1', 'password2','is_active','is_staff', 'is_superuser',
                                        'groups', 'user_permissions'),
        }),
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin_Token_Book, AdminTokenAdmin)

admin.site.register(Boat_Details,BoatAdmin)
admin.site.register(Token_Book,TokenAdmin)
admin.site.register(Crew,CrewAdmin)