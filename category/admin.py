from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
    list_display = ['name', 'slug']