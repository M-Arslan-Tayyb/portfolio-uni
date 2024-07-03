from django.contrib import admin
from contact.models import contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


admin.site.register(contact, ContactAdmin)
# Register your models here.