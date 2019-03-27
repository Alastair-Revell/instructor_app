from django.contrib import admin
from .models import Instructors, InstructorSeries, InstructorCategory

# Register your models here.
class InstructorsAdmin(admin.ModelAdmin):

    fieldsets = [
        ("name/age", {"fields": ["instructor_name", "instructor_age"]}),
        ("price", {"fields": ["instructor_price"]}),
        ("image", {"fields": ["instructor_image"]}),
        ("URL", {"fields": ["instructor_slug"]}),
        ("series", {"fields": ["instructor_series"]}),
    ]

admin.site.register(InstructorSeries)
admin.site.register(InstructorCategory)
admin.site.register(Instructors, InstructorsAdmin)
