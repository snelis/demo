from django.conf.urls import patterns, include, url
from firstapp.views import MyFirstView

urlpatterns = patterns('',
    url(r'', MyFirstView.as_view()),
)
