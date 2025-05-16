from django.contrib import admin

from .models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "short_content", "created_at"]
    search_fields = ["title", "author"]
    list_filter = ["author", "created_at"]
    list_per_page = 10
    readonly_fields = ["id", "created_at", "updated_at"]
