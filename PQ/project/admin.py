from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(projects)
admin.site.register(bids)
#admin.site.register(bid_BOQ)
