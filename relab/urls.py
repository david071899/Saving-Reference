from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.views import crawler,select,ending,display,profile,search
from views import login,logout
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$',login),
    url(r'^search/$',search),
    url(r'^profile/$',profile),
    url(r'^logout/$',logout),
    url(r'^crawler/$',crawler),
    url(r'^crawler/select/$',select),
    url(r'^crawler/select/Add_Success/$',ending),
    url(r'^collection_display/$',display),
)
