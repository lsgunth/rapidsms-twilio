from django.urls import re_path

from rtwilio import views


urlpatterns = [
    re_path(r'^status-callback/$', views.status_callback, name='twilio-status-callback'),
    re_path(r'^$',
        views.validate_twilio_signature(views.TwilioBackendView.as_view()), name='twilio-backend'),
]
