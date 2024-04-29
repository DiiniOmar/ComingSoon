from django.contrib import admin
from Website.models import SignUp

class SingUpAdmin(admin.ModelAdmin):
    list_display= ['id','name', 'email', 'phone']
    
admin.site.register(SignUp, SingUpAdmin)