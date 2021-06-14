from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Blog, Account

# Register your models here.

class AccountAdmin(UserAdmin):
    
    list_display = ('name', 'username', 'email', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('name', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created', 'updated')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Account, AccountAdmin)
