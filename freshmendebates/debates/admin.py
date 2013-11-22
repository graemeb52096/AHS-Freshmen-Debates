from django.contrib import admin
from debates.models import Topic,Location,Date,Teacher,Affirmative,Negative,SubmittedAffirmativeScores,SubmittedNegativeScores

admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(Teacher)
admin.site.register(SubmittedAffirmativeScores)
admin.site.register(SubmittedNegativeScores)

