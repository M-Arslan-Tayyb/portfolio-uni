from django.contrib import admin
from Introduction.models import intro


# Register your models here.
class PersonalInfo(admin.ModelAdmin):
    list_display = ('name', 'skill', 'subject', 'aboutme', 'teach_stack', 'education', 'experience')


admin.site.register(intro, PersonalInfo)
