from django.contrib import admin

# Register your models here.
from social_network.facebook.models import FacebookUser, Photos, Videos

admin.site.register(FacebookUser)
admin.site.register(Photos)
admin.site.register(Videos)
