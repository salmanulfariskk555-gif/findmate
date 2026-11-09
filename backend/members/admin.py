from django.contrib import admin
from .models import Profile,Like,Block,Report
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=("display_name","city","visible","approved","created_at")
    list_filter=("visible","approved")
    search_fields=("display_name","user__username")
    actions=["approve_profiles"]
    @admin.action(description="Approve selected profiles")
    def approve_profiles(self,request,queryset):
        queryset.update(approved=True)
admin.site.register([Like,Block,Report])
