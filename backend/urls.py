from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # paths will be declared here 
    path('',Home, name='home'),
    path('about',About),
    path('contact',Contact),
    path('programs',Programs),
    path('reverse-pitch',Reverseptich),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('events',Events),
    path('sign',Signup, name='sign-up'),
    path('form1',FormsStudent),
    path('form3',FormsStartup),
    path('form2',Formsreversepitch),
    path('rp',ReversePitch),
    path('building',Building),
    path('register',Registration),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)