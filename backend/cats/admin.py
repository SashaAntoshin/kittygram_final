"""Admin configuration for Cats app."""
from django.contrib import admin
from .models import Cat

admin.site.register(Cat)
