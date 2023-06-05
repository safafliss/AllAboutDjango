from django.contrib import admin
from .models import Person
# Register your models here.

#admin.site.register(Person) ==== @admin.register(Person)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):    
    search_fields = ['username']
   