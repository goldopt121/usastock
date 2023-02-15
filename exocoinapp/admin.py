from django.contrib import admin
from .models import Member, Manage, History, Ref

# Register your models here.
admin.site.register(Member)
admin.site.register(Manage)
admin.site.register(History)
admin.site.register(Ref)