from django.contrib import admin
from cmdb import models
# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Host)
admin.site.register(models.Business)
admin.site.register(models.Application)
