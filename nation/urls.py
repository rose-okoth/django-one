from django.conf.urls import url,include
from django.contrib import admin
from django.urls import include, path
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('quotes.urls')),
    path('accounts/register/',
        RegistrationView.as_view(success_url='/profile/'),
        name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]