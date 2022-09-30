from django.shortcuts import render

# Create your views here.

from wiki.models import Page
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
import markdown
from django.template import RequestContext

def index(request):
    #return HttpResponse("Hello, world. You're at the wikicamp index.")
    page_list = Page.objects.all().order_by('name')
    return render_to_response('index.html', {'page_list': page_list})

def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
    except Page.DoesNotExist:
        c = {"page_name": page_name}
        c.update(csrf(request))
        return render_to_response("create.html", c)

    content = page.content
    c = {"page_name": page_name, "content": markdown.markdown(content)}
    c.update(csrf(request))

    context_instance=RequestContext(request)
    context_instance.autoescape=False

    return render_to_response("view.html", c, context_instance)

def edit_page(request, page_name):
    try:
	page = Page.objects.get(pk=page_name)
	content	= page.content
    except Page.DoesNotExist:
	content	= ""
    c = {"page_name": page_name, "content":content}   
    c.update(csrf(request))
    return render_to_response("edit.html", c)

def save_page(request, page_name):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=page_name)
        page.content = content
    except Page.DoesNotExist:
	page = Page(name=page_name, content=content)
    page.save()
    return HttpResponseRedirect("/wikicamp/"+ page_name + "/")


