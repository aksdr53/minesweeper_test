from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('new', views.new, name='new'),
    path('turn', views.turn, name='turn'),

]
