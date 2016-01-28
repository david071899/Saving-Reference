from django.contrib import admin
from website.models import Tag,Art,Collection
# Register your models here.

class CollectionAdmin(admin.ModelAdmin):
	list_display=['collecter']

class ArtAdmin(admin.ModelAdmin):
	list_display=('name','adder')


class TagAdmin(admin.ModelAdmin):
	list_display=('art','style','description','pic_url')

admin.site.register(Collection,CollectionAdmin)
admin.site.register(Art,ArtAdmin)
admin.site.register(Tag,TagAdmin)