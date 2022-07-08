from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Fileupload)
admin.site.register(Story)
admin.site.register(Story_emotions)
admin.site.register(Post_emotions)
admin.site.register(Fileuploadpost)
admin.site.register(Saved)