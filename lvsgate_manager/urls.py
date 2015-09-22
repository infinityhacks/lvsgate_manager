from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lvsgate_manager.views.home', name='home'),
    url(r'^lvsgate/$', 'lvsgate_manager.views.home', name='home'),
    url(r'^lvsgate/vs/$', 'lvsgate_manager.views.list_vs'),
    url(r'^lvsgate/vs/add/$', 'lvsgate_manager.views.add_vs'),
    url(r'^lvsgate/vs/del/$', 'lvsgate_manager.views.del_vs'),

    url(r'^lvsgate/localaddress/$', 'lvsgate_manager.views.list_localaddress'),
    url(r'^lvsgate/localaddress/add/$', 'lvsgate_manager.views.add_localaddress'),
    url(r'^lvsgate/localaddress/del/$', 'lvsgate_manager.views.del_localaddress'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'redirect_field_name': 'next'}),
)
