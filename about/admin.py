from django.contrib import admin
# Register your models here.
from .models import Category, About
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category, CategoryAdmin)

class AboutAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('title','author','published')
    search_fields=('title','content','author__username','categories__name' )
    date_hierarchy='published'
    list_filter=('author__username', 'categories__name')
admin.site.register(About, AboutAdmin)