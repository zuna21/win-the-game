from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/<str:pk>/', views.game, name='game'),
    path('history/', views.history, name='history'),
    path('reply/<str:pk>/', views.reply, name='reply'),
    path('premium/', views.premium, name='premium'),
    path('contact/', views.contact, name='contact'),
]