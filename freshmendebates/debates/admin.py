from django.contrib import admin
from debates.models import Topic,Location,Date,Teacher,Affirmative,Negative,SubmittedAffirmativeScore,SubmittedNegativeScore


admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(Teacher)
admin.site.register(SubmittedAffirmativeScore)
admin.site.register(SubmittedNegativeScore)
