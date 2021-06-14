from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views import debug
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/', debug.default_urlconf, name='django'),
    path('', include('siperkap.urls')),
]

handler404 = 'siperkap.views.handler404'
