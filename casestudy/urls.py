"""casestudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from details import views

urlpatterns = [
    url(r'^$', views.LandingPage.as_view(), name='index'),
    url(r'^list/$', views.BioDataCreate.as_view(), name='biodata-create'),
    url(r'^add/$', views.BioDataList.as_view(), name='biodata-list'),
    #url(r'^dets/', include('details.urls')),
    url(r'^admin/', admin.site.urls),
]
