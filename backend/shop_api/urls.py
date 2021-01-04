from django.conf.urls import url, include

accounts_urlpatterns = [
    url(r'^api/', include('djoser.urls')),
    url(r'^api/', include('djoser.urls.authtoken')),
]