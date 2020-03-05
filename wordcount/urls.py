
from django.urls import path
from . import views
# the . is to import from the current directory


urlpatterns = [
    path("", views.homepage, name="home"),
    path("count/", views.count, name="count"),
    path("about/", views.about, name="about"),
]
