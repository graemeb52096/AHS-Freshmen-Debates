from django.contrib import admin
from blog.models import debate

class DebateAdmin(admin.ModelAdmin):
	#fields display on change list
	list_display = ['topic']
	#fields to filter the change list with
	list_filter = ['date','location','period']
	#fields to search in change list
	search_fields = ['topic','affirmative_team_name','negative_team_name','period','date','location']
	#enable the date drill down on change list
	date_hierarchy = 'date'
	#enable the save buttons on top on change form
	save_on_top = True
	#prepoulate the period, location and date. Need to figure out how to do that.
	#prepoulated_fields = {"period":("title",)}

admin.site.register(debate,DebateAdmin)