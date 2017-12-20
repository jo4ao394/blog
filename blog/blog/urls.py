
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', include('article.urls', namespace='article')),
    url(r'^main/', include('main.urls', namespace='main')),
    url(r'^.*', include('main.urls')),
]
