from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
#importo los valores del script 
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'subetechv1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^acerca_de/', 'frontend.views.aboutus', name='aboutus'),
    url(r'^comentario/', 'frontend.views.coment', name='comentario'),
    url(r'^gracias/', 'frontend.views.gracias', name='gracias'),
    url(r'^paypal/', 'frontend.views.paypal', name='paypal'),
    url(r'^gps/', 'frontend.views.gps', name='gps'),
)

############## LOCATE STATICS


if settings.DEBUG:
	urlpatterns+=  static(settings.STATIC_URL,
						document_root= settings.STATIC_ROOT)
	urlpatterns+=  static(settings.MEDIA_URL,
					document_root= settings.MEDIA_ROOT)
