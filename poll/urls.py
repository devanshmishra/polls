from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^list/$', views.list, name="list"),
    url(r'^codenow/$', views.code_now, name="codenow"),
    url(r'^about/$', views.about_us, name="about"),
    url(r'^article/$', views.articles_list, name="articles"),
    url(r'^codeScripts/$', views.code_scripts, name="codeScripts"),

]
