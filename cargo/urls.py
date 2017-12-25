from django.conf.urls import url, include
from django.contrib import admin
from .views import home_page, RouteListView, RouteCreateView, RouteEditView, RouteDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^acconts/', include('allauth.urls')),
    url(r'^routes/$', RouteListView.as_view(), name='route_list'),
    url(r'^route/create/$', RouteCreateView.as_view(), name='route_create'),
    url(r'^route/(?P<pk>\d+)/update/$', RouteEditView.as_view(), name='route_update'),
    url(r'^route/(?P<pk>\d+)/delete/$', RouteDeleteView.as_view(), name='route_delete')
]
