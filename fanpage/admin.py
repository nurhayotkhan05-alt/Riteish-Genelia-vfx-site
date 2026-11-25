from django.contrib import admin
from .models import SiteContent, Film, TimelineMoment, FamilyMember, GalleryImage

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "genre", "order")
    list_editable = ("order",)
    search_fields = ("title", "description")

@admin.register(TimelineMoment)
class TimelineMomentAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "order")
    list_editable = ("order",)

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order")
    list_editable = ("order",)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
