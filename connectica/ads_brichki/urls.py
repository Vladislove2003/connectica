from django.urls import path
from . import views


app_name = 'ads_brichki'


urlpatterns = [
    path('', views.UsersAdsView.as_view(), name='main'),
]