from django.contrib import admin
from .models import Post, Comments, Likes
from django.utils.html import format_html

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'image_preview', 'author', 'date')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description', 'author')
    readonly_fields = ('image_preview',)
    fieldsets = (
        ('Post Information', {
            'fields': ('title', 'description', 'author', 'date')
        }),
        ('Image', {
            'fields': ('img', 'image_preview'),
        }),
    )
    
    def short_description(self, obj):
        """Return a truncated version of the description"""
        return obj.description[:100] + '...' if len(obj.description) > 100 else obj.description
    short_description.short_description = 'Description'
    
    def image_preview(self, obj):
        """Show image preview in admin panel"""
        if obj.img:
            return format_html('<img src="{}" width="100" height="auto" />', obj.img.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date')
    list_filter = ('post', 'date')
    search_fields = ('name', 'email', 'text_comments')

@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('ip', 'pos')
    list_filter = ('pos',)