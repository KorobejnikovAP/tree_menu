from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.IndexMenuPage.as_view(), name='index')
]