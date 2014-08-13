"""
URLConf for Django user registration and authentication.

Recommended usage is a call to ``include()`` in your project's root
URLConf to include this URLConf for any URL beginning with
``/accounts/``.

"""


from django.conf.urls import *
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views
from registration.views import activate
from registration.views import register
from registration.forms import RegistrationFormUniqueEmail
from userprofile.views import EditProfile, myprofile
from friendship.views import friendship_add_friend
from nxt.views import search
urlpatterns = patterns('',
       # Activation keys get matched by \w+ instead of the more specific
       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
        # that way it can return a sensible "invalid key" message instead of a
        # confusing 404.
          url(r'^activate/(?P<activation_key>\w+)/$',
              activate,
              name='registration_activate'),
          url(r'^login/$', auth_views.login,
            {'template_name': 'registration/login.html'},
              name='auth_login'),
          url(r'^logout/$', auth_views.logout,
             {'template_name': 'registration/logout.html'},
              name='auth_logout'),
          url(r'^password/change/$', auth_views.password_change,
             name='auth_password_change'),
           url(r'^password/change/done/$',
                 auth_views.password_change_done,
              name='auth_password_change_done'),
           url(r'^password/reset/$',
               auth_views.password_reset,
              name='auth_password_reset'),
           url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,                          name='auth_password_reset_confirm'),
            url(r'^password/reset/complete/$',
               auth_views.password_reset_complete,
            name='auth_password_reset_complete'),
            url(r'^password/reset/done/$',
              auth_views.password_reset_done,
              name='auth_password_reset_done'),
            url(r'^/?$', register,{'form_class': RegistrationFormUniqueEmail},  name='registration_register'),
            url(r'^myprofile/$', myprofile, name='myprofile'),
            url(r'^register/complete/$',TemplateView.as_view
            (template_name= 'registration_complete.html'),name='registration_complete'),
            url(r'^profile/$', EditProfile, name='edit_profile'),
            url(r'^friends/$',include('friendship.urls')),
            url(r'^profile/search/$', search, name='search'),
            )
