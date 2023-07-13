from django.contrib import admin
from .models import post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_created')

admin.site.register(post,PostAdmin)