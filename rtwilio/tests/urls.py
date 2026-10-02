from django.urls import include, re_path


urlpatterns = [
    re_path(r'^backend/twilio/', include('rtwilio.urls')),
]
