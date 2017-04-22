from django.contrib import admin
from poll.models import Post, Document, Article, listCodeScript
from poll.models import Share

# Register your models here.
admin.site.register(Post)
admin.site.register(Share)

admin.site.register(Document)
admin.site.register(Article)
admin.site.register( listCodeScript)