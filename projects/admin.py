from django.contrib import admin
from .models import Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(Contact, ContactAdmin)
