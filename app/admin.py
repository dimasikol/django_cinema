from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cinema,Actors,Genres


@admin.register(Cinema)
class AdminCinema(admin.ModelAdmin):
    list_display = ('id','name','date','get_image','date_update','cinema')
    list_editable = ('name','date')

    def get_image(self,obj):
            return mark_safe(f'<img src="{obj.preview_image.url}" width="50" height="60"/>')
    get_image.allow_rags=True



@admin.register(Actors)
class AdminActors(admin.ModelAdmin):
    pass

@admin.register(Genres)
class AdminGenres(admin.ModelAdmin):
    pass


