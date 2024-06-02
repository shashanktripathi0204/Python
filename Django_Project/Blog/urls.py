from django.urls import path
# . is for current directory
from . import views

urlpatterns = [
    # empty path "", view.home-> is what will be present at ""
    path("", views.home, name = "blog-home"),
    path("about/", views.about, name = "blog-about"),
]