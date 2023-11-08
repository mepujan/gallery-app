from django.urls import path
from .views import homepage
app_name = 'gallery'

urlpatterns = [
    path("", homepage, name="homepage")
]
