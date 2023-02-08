from django.contrib import admin
from coaches.models import Coaches

@admin.register(Coaches)
class CoachesAdmin(admin.ModelAdmin):
    list_display = ('name', 'background', 'imagepop')