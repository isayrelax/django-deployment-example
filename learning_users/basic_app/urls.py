from django.conf.urls import url, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^registration/$', views.registration, name='registration'),
    url(r'user_login/$', views.user_login, name='user_login'),
]