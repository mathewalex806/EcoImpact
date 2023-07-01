from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(User)
admin.site.register(Airtravel)
admin.site.register(Roadtravel)
admin.site.register(Seatravel)
admin.site.register(Info)
admin.site.register(Energy)
admin.site.register(Goods)
