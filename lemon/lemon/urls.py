from django.contrib import admin 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from LittleLemonAPI.views import BookingViewSet

router = DefaultRouter()
router.register(r'booking', BookingViewSet)
 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('restaurant.urls')),
    path('menu/',include('restaurant.urls')),
    path('booking/', include(router.urls)),
    path('api/',include('LittleLemonAPI.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

