from django.urls import path
from server.apps.githubinfo.views import create, detail

app_name = 'githubinfo'

urlpatterns = [
    path('create', create, name='create'),
    path('detail', detail, name='detail'),

]
