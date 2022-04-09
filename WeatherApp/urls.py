from django.urls import path
from .views import *
app_name = 'WeatherApp'
urlpatterns =[
    
    path('', CityWeatherView, name='city_weather'),
    path('remove/<city_name>/', City_delete, name='city_remove'),
    ]