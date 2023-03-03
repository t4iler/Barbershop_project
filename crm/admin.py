from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm



class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('commented_at', 'comment_text')
    readonly_fields = ('commented_at',)
    extra = 0 


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'ordered_at',)
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone',)
    list_per_page = 10
    list_max_show_all = 50
    fields = ('id', 'order_status', 'ordered_at', 'order_name', 'order_phone',)
    readonly_fields = ('id', 'ordered_at',)
    # поле класса Коммент
    inlines = [Comment,]



admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)