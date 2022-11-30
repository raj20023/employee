from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
    # path for employee table
    path('employee-list',views.employeelist, name='employee-list'),
    path('employee-detail/<str:pk>',views.employeedetail,name='employee-detail'),
    path('emp-create/',views.employeecreate,name="new-employee"),
    path('emp-update/<str:pk>/',views.employeeupdate,name='emp-upadate'),
    path('emp-delete/<str:pk>/',views.employeedelete,name='emp-delete'),
    # path for company table
    path('cmp-list',views.companylist, name='company-list'),
    path('cmp-detail/<str:pk>/',views.companydetail,name='company-detail'),
    path('cmp-create/',views.companycreate,name="new-company"),
    path('cmp-update/<str:pk>/',views.companyupdate,name='cmp-upadate'),
    path('cmp-delete/<str:pk>/',views.companydelete,name='cmp-delete')
]