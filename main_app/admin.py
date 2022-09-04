from django.contrib import admin
from .models import Nft, Rating, Chain

# Register your models here.
admin.site.register(Nft)
admin.site.register(Rating)
admin.site.register(Chain)