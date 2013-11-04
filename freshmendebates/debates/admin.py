from django.contrib import admin
from debates.models import Topic,Location,Date,Teacher
from debates.forms import AffirmativeScore,NegativeScore

admin.site.register(Topic)
admin.site.register(Location)
admin.site.register(Date)
admin.site.register(Teacher)


