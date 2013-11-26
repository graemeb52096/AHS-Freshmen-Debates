from django.contrib import admin
from debates.models import Topic,Location,Date,Teacher,Affirmative,Negative,SubmittedAffirmativeScore,SubmittedNegativeScore

class AffSubmitAdmin(admin.ModelAdmin):
	list_display = ['Speaker1','Speaker2','CrossExamination','Argument','SlideShowScore','TeamNumber']
	search_fields = ['TeamNumber']

class NegSubmitAdmin(admin.ModelAdmin):
	list_display = ['Speaker1','Speaker2','CrossExamination','Argument','SlideShowScore','TeamNumber']
	search_fields = ['TeamNumber']

admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(Teacher)
admin.site.register(SubmittedAffirmativeScore, AffSubmitAdmin)
admin.site.register(SubmittedNegativeScore, NegSubmitAdmin)

