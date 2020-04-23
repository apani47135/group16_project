from django.contrib import admin
from .models import Packages, Sender, branches, reciever, package_history, location_mark

admin.site.register(Sender)
admin.site.register(Packages)
admin.site.register(branches)
admin.site.register(reciever)
admin.site.register(location_mark)