# Register your models here.
from django.contrib import admin


from myapp.models import Country, MyUser

admin.site.register(Country)
admin.site.register(MyUser)
