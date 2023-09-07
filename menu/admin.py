from django.contrib import admin
from .models import Menu
# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Menu,MenuAdmin)
