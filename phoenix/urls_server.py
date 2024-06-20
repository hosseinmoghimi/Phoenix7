 
from django.contrib import admin
from django.urls import path,include,re_path
from phoenix.settings import PUBLIC_ROOT
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT, DEBUG,QRCODE_ROOT
from django.views.static import serve
print(STATIC_ROOT)
print(MEDIA_ROOT)
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('market/', include('market.urls')),
    path('authentication/', include('authentication.urls')),
    path('utility/', include('utility.urls')),
    
    
    re_path(r'^qrcode/(?P<path>.*)$', serve, {'document_root': QRCODE_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
