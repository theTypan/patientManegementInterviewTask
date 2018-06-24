from django.conf.urls import url

from departments import views

urlpatterns = [
    url(
    	r'^$', 
    	views.DepartmentListCreateAPIView.as_view(), 
    	name="department_list_create"
    ),
    url(
    	r'^(?P<pk>[^/]+)/$', 
    	views.DepartmentRetrieveUpdateDestroyView.as_view(), 
    	name="department_retrieve_update_destroy"
    ),
     url(
        r'^patients$', 
        views.DepartmentPatientListCreateAPIView.as_view(), 
        name="department_patient_list_create"
    ),
    url(
        r'^patients/(?P<pk>[^/]+)/$', 
        views.DepartmentPatientRetrieveUpdateDestroyView.as_view(), 
        name="department_patient_retrieve_update_destroy"
    ),
]