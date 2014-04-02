from django.contrib import admin
admin.autodiscover()
from django.db import models

from debates.models import *
from debates.forms import *

#def order_by_teacher(modeladmin, request, queryset):

class TeamAdmin(admin.ModelAdmin):
    list_filter = ['teacher']
    ordering = ['team_Number']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','englishTeacher','IHSTeacher')
    ordering = ['last_name']
    list_filter = ['englishTeacher','IHSTeacher','englishPeriod']

class DateAdmin(admin.ModelAdmin):
    ordering = ['date']
    

admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(SubmittedAffirmativeScore)
admin.site.register(SubmittedNegativeScore)
admin.site.register(School)
admin.site.register(GoogleUser)
admin.site.register(Student, StudentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Debate)
admin.site.register(Period)





try:
	from admin_import.options import add_import
except ImportError:
	pass
else:
		add_import(InviteeAdmin)