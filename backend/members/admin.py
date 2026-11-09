from django.contrib import admin
from .models import Profile, Like, Block, Report

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "city", "visible", "approved", "created_at")
    list_filter = ("visible", "approved")
    search_fields = ("display_name", "user__username")
    actions = ["approve_profiles", "hide_profiles"]

    @admin.action(description="Approve selected profiles")
    def approve_profiles(self, request, queryset):
        queryset.update(approved=True)

    @admin.action(description="Hide selected profiles from discovery")
    def hide_profiles(self, request, queryset):
        queryset.update(visible=False)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "reporter", "reported", "reason", "created_at")
    list_filter = ("created_at",)
    search_fields = ("reporter__username", "reported__username", "reason")
    readonly_fields = ("reporter", "reported", "reason", "created_at")

admin.site.register([Like, Block])
