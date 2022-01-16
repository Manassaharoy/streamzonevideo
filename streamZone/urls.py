from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('AppLogin.urls')),
    path('videos/', include('AppVideo.urls')),
    path('', views.Homepage, name='home'),
    path('error/', views.errorpage, name='error'),

]

handler404="streamZone.views.handler_not_found"

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)