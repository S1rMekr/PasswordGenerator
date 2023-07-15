from django.urls import path
from PasswordGenerator.views import *

urlpatterns = [
    path('', index),
    path('generator', generator, name='generator')
]
