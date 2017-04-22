from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=360)
    created_at = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Share(models.Model):
    user = models.ForeignKey('auth.User')
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.likes


class Document(models.Model):
    docfile = models.FileField(upload_to='document/%y/%m/%d')

    # store file in media/documents/2017/03/30
    def upload(self):
        self.save()

    def __str__(self):
        return self.docfile.path


class listCodeScript(models.Model):
    title = models.CharField(max_length=25)
    banner = models.FileField(upload_to='codescript/%y/%m/%d')
    html_file_path = models.FileField(upload_to='codescript')
    css_file_path = models.FileField(upload_to='codescript')
    js_file_path = models.FileField(upload_to='codescript')
    creator = models.ForeignKey('auth.User')
    created_at = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField(default=0)

    def upload(self):
        self.save()

    def __str__(self):
        return self.title


class Article(models.Model):
    banner = models.FileField(upload_to='article/%y/%m/%d')
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=20,
                                choices=(("html", "html"), ("css", "css"), ("js", "javascript"), ("all", "Other")))
    content = models.TextField(max_length=65000)
    created_at = models.DateTimeField(default=timezone.now)

    # store file in media/articles/2017/03/30
    def upload(self):
        self.save()

    def __str__(self):
        return self.title
