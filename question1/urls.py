from django.urls import path
from .views import NavigationRecordAPI

urlpatterns = [
    path('navigation/', NavigationRecordAPI.as_view()),
]