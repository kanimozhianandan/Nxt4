try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns
from django.views.generic import TemplateView
from friendship.views import view_friends, friendship_add_friend, friendship_accept, \
friendship_reject, friendship_cancel, friendship_request_list, \
friendship_request_list_rejected, friendship_requests_detail, followers,\
following, follower_add, follower_remove, sortby_users, friend_invite, add_counselor
from userprofile.views import EditProfile
urlpatterns = patterns('',
    url(r'^profile/$', TemplateView.as_view(template_name='friendship/sprofile.html') ),
    url(r'^users/$', view=sortby_users,  name='friendship_view_users',
    ),
    url(r'editprofile/$', EditProfile, name="edit_profile" ,),
    url(r'^add/$', add_counselor, name='follow my counselor'),
    url(r'^friends/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        view_friends,
        'friendship_view_friends',
    ),
    url(r'^friend/add/(?P<to_username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        view=friendship_add_friend,
        name='friendship_add_friend',
    ),
    url(
        regex=r'^friend/accept/(?P<friendship_request_id>\d+)/$',
        view=friendship_accept,
        name='friendship_accept',
    ),
    url(
        regex=r'^friend/reject/(?P<friendship_request_id>\d+)/$',
        view=friendship_reject,
        name='friendship_reject',
    ),
    url(
        regex=r'^friend/cancel/(?P<friendship_request_id>\d+)/$',
        view=friendship_cancel,
        name='friendship_cancel',
    ),
    url(
        regex=r'^friend/requests/$',
        view=friendship_request_list,
        name='friendship_request_list',
    ),
    url(
        regex=r'^friend/requests/rejected/$',
        view=friendship_request_list_rejected,
        name='friendship_requests_rejected',
    ),
    url(
        regex=r'^friend/request/(?P<friendship_request_id>\d+)/$',
        view = friendship_requests_detail,
        name='friendship_requests_detail',
    ),
    url(
        regex=r'^followers/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        view=followers,
        name='friendship_followers',
    ),
    url(
        regex=r'^following/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        view=following,
        name='friendship_following',
    ),
    url(
       regex = r'^follower/add/(?P<femail>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', view=follower_add, name='follower_add',
    ),
    url(r'^follower/remove/(?P<followee_email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',follower_remove,'follower_remove',
    ),

    url(r'^friends/invite/$', friend_invite, name='friend_invite'),
            )
