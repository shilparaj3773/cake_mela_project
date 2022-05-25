from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.customer)
admin.site.register(models.cake)
admin.site.register(models.orderplaced)
admin.site.register(models.payment)
