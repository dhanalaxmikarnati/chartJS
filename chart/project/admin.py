from django.contrib import admin

# Register your models here.
from .models import Dashboard

@admin.register(Dashboard)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'sector','topic' ,'country', 'published','intensity')
    search_fields = ['title', 'sector', 'country']
    list_filter = ('sector', 'country', 'published')