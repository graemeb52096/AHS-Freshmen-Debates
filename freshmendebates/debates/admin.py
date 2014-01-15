from django.contrib import admin
from debates.models import Topic,Location,Date,Affirmative,Negative,SubmittedAffirmativeScore,SubmittedNegativeScore,School,GoogleUser,Student,Team,Debate


admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(SubmittedAffirmativeScore)
admin.site.register(SubmittedNegativeScore)
admin.site.register(School)
admin.site.register(GoogleUser)
admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Debate)




try:
	from admin_import.options import add_import
except ImportError:
	pass
else:
		add_import(InviteeAdmin)