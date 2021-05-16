from django.contrib import admin

from .models import Animal, Category

# admin.site.register(Category)
# admin.site.register(Animal)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
