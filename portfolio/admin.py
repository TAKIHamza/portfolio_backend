from django.contrib import admin
from .models import Profile, Project, ProjectImage, Skill, ContactSubmission

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ['title', 'user', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(ContactSubmission)