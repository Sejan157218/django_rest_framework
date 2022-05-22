from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverviews,name='api-overview'),
]
