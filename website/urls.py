from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url('^admin/', admin.site.urls),
    path('',include('my_app.urls'))
]
