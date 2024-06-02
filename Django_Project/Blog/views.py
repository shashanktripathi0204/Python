from django.shortcuts import render
from django.http import HttpResponse


# Home will be responsible for handling the traffic at the home page of our blog
def home(request):
    # we return what we want the user to see when he is sent to the route
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')