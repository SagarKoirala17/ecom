from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','message')
    list_display_links = ('first_name','email')
    search_fields = ('first_name','email')
    list_per_page = 25


admin.site.register(Contact,ContactAdmin)
