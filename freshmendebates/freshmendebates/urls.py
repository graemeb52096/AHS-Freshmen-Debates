from django.conf.urls import patterns, include, url

# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$','debates.views.Aff'),
	url(r'^$','debates.views.Neg'),
	url(r'^post/Affscoring_upload.html$', 'debates.views.Aff', name='judging'),
	url(r'^post/Negscoring_upload.html$', 'debates.views.Neg', name='judging'),   
    # Examples:
    # url(r'^$', 'freshmendebates.views.home', name='home'),
    # url(r'^freshmendebates/', include('freshmendebates.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
