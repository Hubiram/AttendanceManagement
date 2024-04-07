from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('attendance.urls')),
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
]
