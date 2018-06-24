from django.conf.urls import url

from locations import views

urlpatterns = [
    url(
    	r'^counties/$', 
    	views.CountyListCreateAPIView.as_view(), 
    	name="county_list_create"
    ),
    url(
    	r'^counties/(?P<pk>[^/]+)/$', 
    	views.CountyRetrieveUpdateDestroyView.as_view(), 
    	name="county_retrieve_update_destroy"
    ),
    url(
        r'^subcounties/$', 
        views.SubcountyListCreateAPIView.as_view(), 
        name="subcounty_list_create"
    ),
    url(
        r'^subcounties/(?P<pk>[^/]+)/$', 
        views.SubcountyRetrieveUpdateDestroyView.as_view(), 
        name="subcounty_retrieve_update_destroy"
    ),
    url(
        r'^wards/$', 
        views.WardListCreateAPIView.as_view(), 
        name="ward_list_create"
    ),
    url(
        r'^wards/(?P<pk>[^/]+)/$', 
        views.WardRetrieveUpdateDestroyView.as_view(), 
        name="ward_retrieve_update_destroy"
    ),
    url(
        r'^villages/$', 
        views.VillageListCreateAPIView.as_view(), 
        name="ward_list_create"
    ),
    url(
        r'^villages/(?P<pk>[^/]+)/$', 
        views.VillageRetrieveUpdateDestroyView.as_view(), 
        name="ward_retrieve_update_destroy"
    ),
]