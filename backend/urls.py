from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # paths will be declared here 
    path('',Home),
    path('/about',About),
    path('/contact',Contact),
    path('/programs',Programs),
    path('/reverse-pitch',Reverseptich),
    path('/sign-up',Signup),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)