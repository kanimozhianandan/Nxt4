from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from registration.forms import add_college_form
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url
from django import template
from django.template import RequestContext
from collegelist.models import collegelist
@login_required
def addcollege(request):
    if request.method == 'POST':
        form = add_college_form(request.POST)
        if form.is_valid():
            college = form.save(commit=False)
            college.user = request.user
            college.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
       form = add_college_form()

    args = {}
    args.update(csrf(request))
    args['form']=form

    return render_to_response("django_messages/subvtle.html",args)


def getcollege(request):
    user = request.user
    colleges = collegelist.objects.filter(user=user)
    return render_to_response("add_post.html", {'colleges':colleges} )
