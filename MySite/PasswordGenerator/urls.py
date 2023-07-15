from django.urls import path
from PasswordGenerator.views import *

urlpatterns = [
    path('', index, name='home'),
    path('generator', generator, name='generator')
]
