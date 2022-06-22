from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('booking/', views.booking, name='booking'),
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

