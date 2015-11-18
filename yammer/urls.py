"""Defines the URL routes for this app."""

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import YammerView

urlpatterns = patterns(
    'yammer.views',
    url(r"^/$", login_required(YammerView.as_view()), name="yammer")
)
