try:
    from django.conf.urls import url, patterns
except ImportError:
    from django.conf.urls.defaults import url, patterns
from friendship.views import view_friends, friendship_add_friend, friendship_accept, \
friendship_reject, friendship_cancel, friendship_request_list, \
friendship_request_list_rejected, friendship_requests_detail, followers,\
following, follower_add, follower_remove, all_users

urlpatterns = patterns('',
    url(
        r'^users/$',
        all_users,
        name='friendship_view_users',
    ),
    url(
        r'^friends/(?P<username>[\w-]+)/$',
        view_friends,
        'friendship_view_friends',
    ),
    url(
        r'^/add/(?P<to_username>[\w-]+)/$',
        friendship_add_friend,
        'friendship_add_friend',
    ),
    url(
        r'^friend/accept/(?P<friendship_request_id>\d+)/$',
        friendship_accept,
        'friendship_accept',
    ),
    url(
        r'^friend/reject/(?P<friendship_request_id>\d+)/$',
        friendship_reject,
        'friendship_reject',
    ),
    url(
        r'^friend/cancel/(?P<friendship_request_id>\d+)/$',
        friendship_cancel,
        'friendship_cancel',
    ),
    url(
        r'^friend/requests/$',
        friendship_request_list,
        'friendship_request_list',
    ),
    url(
        r'^friend/requests/rejected/$',
        friendship_request_list_rejected,
        'friendship_requests_rejected',
    ),
    url(
        regex=r'^friend/request/(?P<friendship_request_id>\d+)/$',
        view=friendship_requests_detail,
        name='friendship_requests_detail',
    ),
    #url(
    #   regex=r'^followers/(?P<username>[\w-]+)/$',
    #   view=followers,
    #   name='friendship_followers',
    #),
#url(
 #       regex=r'^following/(?P<username>[\w-]+)/$',
  #      view=following,
   #     name='friendship_following',
    #),
    #url(
     #   regex=r'^follower/add/(?P<followee_username>[\w-]+)/$',
      #  view=follower_add,
       # name='follower_add',
    #),
    #url(
    #    regex=r'^follower/remove/(?P<followee_username>[\w-]+)/$',
     #   view=follower_remove,
      #  name='follower_remove',
    #),
)
