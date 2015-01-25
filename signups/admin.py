from django.contrib import admin

# Register your models here.

from .models import SignUp

class SignupAdmin(admin.ModelAdmin):
    class Meta:
        model = SignUp
 #to be seen int the django admin
admin.site.register(SignUp,SignupAdmin)