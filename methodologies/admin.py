from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'date_added',)

    def get_tags(self, obj):
        return ', '.join([tag.title for tag in obj.tags.all()])

    def view_article(self, obj):
        return mark_safe('<a href="{}" target="_blank">view</a>'.format(obj.url))

admin.site.register(Post, PostAdmin)
