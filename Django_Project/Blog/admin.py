from django.contrib import admin
from .models import Post

# Registering the Post model with admin site
admin.site.register(Post)
