from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'css', 'get_image')
    list_display_links = ('title',)
    list_editable = ('css',)
    fields = ('title', 'description', 'css', 'img', 'get_image')
    readonly_fields = ('get_image',)


    def get_image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="80px"')
        else:
            return 'Нет картинки!'

    get_image.short_description = 'Миниатюра'

admin.site.register(CmsSlider, CmsAdmin)