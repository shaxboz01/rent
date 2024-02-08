from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    # path('about_details', about_details, name='details')
    path('blog/', blog, name='blog'),
    path('car/', car, name='car'),
    path('contact/', contact, name='contact'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]