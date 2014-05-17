from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect

# Create your views here.
def index(request):
    return render_to_response(
        'index.html', 
        {}, 
        context_instance=RequestContext(request)
    )

def search(request):
    return render_to_response(
        'lisa_search/search.html', 
        {}, 
        context_instance=RequestContext(request)
    )
def upload(request):
    return render_to_response(
        'lisa_search/upload.html', 
        {}, 
        context_instance=RequestContext(request)
    )
