from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# # Home will be responsible for handling the traffic at the home page of our blog
# def home(request):
#     # we return what we want the user to see when he is sent to the route
#     return HttpResponse('<h1>Blog Home</h1>')
#
#
# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "Blog/home.html", context)


def about(request):
    return render(request, "Blog/about.html", {"title": "About"})
