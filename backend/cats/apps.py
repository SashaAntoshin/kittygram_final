"""Cats app configuration."""
from django.apps import AppConfig

class CatsConfig(AppConfig):
    """Configuration for Cats application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cats'
