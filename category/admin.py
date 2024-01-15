from django.contrib import admin
from category.models import CategoryModel

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
    list_display = ['name', 'slug']
    
admin.site.register(CategoryModel, CategoryAdmin)