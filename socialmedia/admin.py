from django.contrib import admin

from .models import User,Credential,Comment

admin.site.register(User)
admin.site.register(Credential)
admin.site.register(Comment)
