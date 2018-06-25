from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(
    	r'^users/$', 
    	views.UserListCreateAPIView.as_view(), 
    	name="user_list_create"
    ),
    url(
    	r'^users/(?P<pk>[^/]+)/$', 
    	views.UserRetrieveUpdateDestroyView.as_view(), 
    	name="user_retrieve_update_destroy"
    ),
]