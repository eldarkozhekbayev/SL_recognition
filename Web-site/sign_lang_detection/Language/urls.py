from django.urls import path
from . import views
app_name = 'language'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('convert_to_sign_index/', views.convert_to_sign_index, name='convert_to_sign_index'),
    path('get_letter_images/', views.get_letter_images, name='get_letter_images'),
    path('convert_to_sign/', views.convert_to_sign, name='convert_to_sign'),
    path('alphabet/', views.alphabet, name='alphabet'),
]
