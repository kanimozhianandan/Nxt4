from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django_messages.forms import postfeedForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from userprofile.models import UserProfile
from feeds.models import Feeds
from friendship.models import Friend

@login_required
def main(request):
    email = request.user.profile.counselor_email
    try:
        feed = User.objects.get(email=request.user.profile.counselor_email)
    except:
        feed = UserProfile.objects.get(email=email)
    posts = Feeds.objects.filter(user=feed).order_by("-postdate")
    paginator = Paginator(posts, 5)
    try:
        posts = int(request.GET.get("page","1"))
        page = 2
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage,EmptyPage):
        posts = paginator.page(paginator.num_pages)
    
    return render_to_response("friendship/friend/post.html", dict(posts=posts,user=request.user)) 

@login_required
def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = postfeedForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect("django_messages/subvtle.html")
        else:
            print form.errors
    else:
        form = postfeedForm()
    return render_to_response("django_messages/subvtle.html", context)

def post(request):
    user = request.user
    posts = Feeds.objects.filter(user = request.user)
    d = dict(posts=posts, form=postfeedForm(), user=request.user)
    d.update(csrf(request))
    return render_to_response("django_messages/subvtle.html",d)

"""    
    t = get_template('post.html')
    c = Context({'posts':post})
    return HttpResponse(t.render(c))
"""


