from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.dashboard, name='home'),
    url(r'^activities/$', views.activities, name='activities'),
]
