from django.contrib import admin
from account.models import UserAccount

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','created_at','state_of_origin',]
    list_filter = ['created_at']

admin.site.register(UserAccount, UserAdmin)

