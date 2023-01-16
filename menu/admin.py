from django.contrib import admin

from menu.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'is_visible', 'named_url', )
    list_editable = ('is_visible', )
    # list_filter = ()


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'parent', 'is_visible', )
    list_editable = ('is_visible', )
    list_filter = ('parent',)
