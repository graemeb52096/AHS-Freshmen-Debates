from django.conf.urls import patterns, include, url
# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^Judge$','debates.views.judge'),
	url(r'^SplashPage$','debates.views.splash'),
	url(r'^Teacher$','debates.views.teacher'),
	url(r'^TeacherSelector$','debates.views.teacherselector'),
	url(r'^TeamCreate$','debates.views.teamcreate'),
	url(r'^DebateSelector$','debates.views.debateselector'),
	url(r'^post/scoring_upload.html$', 'debates.views.handle', name='judging'), 
    # Examples:
    # url(r'^$', 'freshmendebates.views.home', name='home'),
    # url(r'^freshmendebates/', include('freshmendebates.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
