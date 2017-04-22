from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.core.urlresolvers import reverse

from poll.forms import DocumentForm
from poll.models import Post, Document, Article, listCodeScript


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html', )


# file upload
def list(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES('docfile'))
            newdoc.save()
            return HttpResponseRedirect('/list')
        else:
            form = DocumentForm()
        documents = DocumentForm()
        documents = Document.objects.all()

        return render(request, 'list.html', {'documents': documents, 'form': form})


def code_now(request):
    return render(request, "CodeNow.html", {})


def code_scripts(request):
    list = listCodeScript.objects.all()
    context = {
        'list': list
    }
    return render(request, "codeScripts.html", {"list": list})


def about_us(request):
    return render(request, "about.html", {})


def articles_list(request):
    list = Article.objects.all()
    return render(request, "article.html", {"list": list})

# def articles_html(request):
#     list = Article.objects.filter('category', 'html')
#     return render(request, "article.html", {"list": list})
