"""Defines the URL routes for this app."""

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from views import YammerTabView

urlpatterns = patterns(
    'yammer.views',
    url(r"^/$", login_required(YammerTabView.as_view()), name="yammer_tab")
)
