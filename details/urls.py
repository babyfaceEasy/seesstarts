from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.LandingPage.as_view(), name='index'),
    url(r'^list/$', views.BioDataCreate.as_view(), name='biodata-create'),
    url(r'^add/$', views.BioDataList.as_view(), name='biodata-list'),
]