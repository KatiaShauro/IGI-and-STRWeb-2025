from django.contrib import admin

from .models import AboutCompany, FAQ


# Register your models here.
@admin.register(AboutCompany)
class AboutCompanyAdmin(admin.ModelAdmin):
    list_display = ["video", "logo", "requisites"]
    search_fields = ["history", "requisites"]
    list_per_page = 10
    readonly_fields = ["id"]
    fieldsets = (
        ("Медиа", {"fields": ("logo", "video")}),
        ("Описание", {"fields": ("history", "requisites")}),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "answer", "answer_date"]
    search_fields = ["question", "answer_date"]
    list_per_page = 10
    readonly_fields = ["id", "answer_date"]
