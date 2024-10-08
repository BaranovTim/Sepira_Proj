from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.remove, name='remove'),
    path('preaction_third/qrcodes/', include('qrcodes.urls')),
    path('preaction_forth/qrcodes/', include('qrcodes.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)