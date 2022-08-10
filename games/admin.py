from django.contrib import admin
from .models import Game, Comment, Reply

# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Reply)