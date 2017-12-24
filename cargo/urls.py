from django.conf.urls import url
from django.contrib import admin
from .views import home_page, RouteListView, RouteCreateView, RouteEditView, RouteDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^routes/$', RouteListView.as_view(), name='route_list'),
    url(r'^route/create/$', RouteCreateView.as_view(), name='route_create'),
    url(r'^route/(?P<pk>\d+)/update/$', RouteEditView.as_view(), name='route_update'),
    url(r'^route/(?P<pk>\d+)/delete/$', RouteDeleteView.as_view(), name='route_delete')
]
