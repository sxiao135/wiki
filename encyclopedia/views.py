from django.shortcuts import render
from django import forms
from django.template import RequestContext
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def handler404(request, *args, **argv):
    response = request('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


# def handler500(request, *args, **argv):
#     response = render_to_response('500.html', {}, context_instance=RequestContext(request))
#     response.status_code = 500
#     return response
# this is the catch all error

class AddPageForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
        })
    )