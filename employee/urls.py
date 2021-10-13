from django.conf.urls import url
from django.urls import path
from employee import views


urlpatterns = [
    url(r'department$', views.department_list, name = 'deparment-list'),
    url(r'employee$', views.employee_list, name = 'employee-list'),

    url(r'department/([0-9]+)$', views.department_detail, name = 'department-detail'),
    
]