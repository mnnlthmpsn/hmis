from django.urls import path
from . import views

app_name = 'administrator'

urlpatterns = [
    # drugs
    path('add/drug/', views.add_drug, name='add_drug'),
    path('drug/all/', views.all_drugs, name='all_drugs'),
    path('update/<str:drug_name>/drug/', views.update_drug, name='update_drug'),

    # staff
    path('add/staff/', views.add_staff, name='add_staff'),
    path('staff/all/', views.all_staff, name='all_staff'),
    path('update/<uuid:staff_id>/staff', views.update_staff, name='update_staff'),

    # logs
    path('logs/', views.logs, name='logs'),

    # sales
    path('sell', views.sell, name='sell'),
    path('sales/today/', views.sales_today, name='sales_today'),
    path('sales/all/', views.all_sales_list, name='all_sales_list'),
    path('sales/shortages/', views.shortage, name='shortage'),
    path('sales/<str:date>/', views.sales_details, name='s_details'),
    
    
]