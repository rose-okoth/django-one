from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.quote_of_day,name='quotesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_quotes,name='pastQuotes'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.post,name ='post')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
