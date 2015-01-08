from django.shortcuts import render

from Blog.models import Post
from django.template import Context, loader, RequestContext, Template
from django.http import HttpResponse

def home(request):
    posts = Post.objects.order_by('-dateCreated').all()
    template = loader.get_template("Blog/home.html")
    context = RequestContext(request, {"posts": posts})
    return HttpResponse(template.render(context))
	
def asteroidField(request):
	return render(request, 'Blog/asteroidField.html')
    