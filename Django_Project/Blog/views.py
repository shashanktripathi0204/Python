from django.shortcuts import render
from django.http import HttpResponse

# # Home will be responsible for handling the traffic at the home page of our blog
# def home(request):
#     # we return what we want the user to see when he is sent to the route
#     return HttpResponse('<h1>Blog Home</h1>')
#
#
# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

posts = [
    {
        "author": "Shashank",
        "title": "Blog Post 1",
        "content": "First Post Content",
        "date_posted": "June 2, 2024"
    },
    {
        "author": "Tripathi",
        "title": "Blog Post 2",
        "content": "Second Post Content",
        "date_posted": "June 3, 2024"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "Blog/home.html", context)


def about(request):
    return render(request, "Blog/about.html", {"title": "About"})
