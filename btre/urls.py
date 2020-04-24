
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
