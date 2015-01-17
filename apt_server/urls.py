from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'exercises.views.home', name='home'),
    url(r'^dashboard/', 'exercises.views.dailyExercises', name = 'dashboard'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
		document_root=settings.STATIC_ROOT)