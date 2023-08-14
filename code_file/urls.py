from django.urls import path
from code_file.views import qrcode_generator

urlpatterns = [
    path('', qrcode_generator, name="qrcode")
]