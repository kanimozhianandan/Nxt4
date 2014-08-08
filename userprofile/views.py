from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django_messages.forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url
from django import template
from django.template import RequestContext

@login_required
def EditProfile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
        # success_url needs to be dynamically generated here; 
            return HttpResponseRedirect('/subvtle/#home');
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance = profile)

    args = {}    
    args.update(csrf(request))
    args['form'] = form

    return render_to_response('registration/edit_profile.html', args)


@login_required
def myprofile(request):
    if request.user.is_authenticated():
        return render_to_response('registration/profile.html',context_instance=RequestContext(request))
