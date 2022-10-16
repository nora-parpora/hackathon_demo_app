from django.contrib import admin


from posts.models import JobAdvert


@admin.register(JobAdvert)
class JobAdmin(admin.ModelAdmin):
    list_display = ('position', 'employment_type')
