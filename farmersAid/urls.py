

from django import urls
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
    path('blog/', include('Blog2.urls')),
    #path('weather_app/', include('weather.urls')),
    #path('weather_app/delete/<int:id>', include('weather.urls')),
    path('weather_app/', include('WeatherApp.urls', namespace='WeatherApp')),
    path('froala_editor/',include('froala_editor.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
