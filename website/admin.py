from django.contrib import admin
from website.models import Tag,Art
# Register your models here.
class ArtAdmin(admin.ModelAdmin):
	list_display=['name']

class TagAdmin(admin.ModelAdmin):
	list_display=('art','style','description','pic_url')

admin.site.register(Art,ArtAdmin)
admin.site.register(Tag,TagAdmin)