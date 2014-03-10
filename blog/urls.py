from django.conf.urls import *
#from django.conf import settings
#from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'blog.views.home', name='home'),
     url(r'^blog/', include('blog.urls')),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls))

) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
