from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.institutionList, name='institutions'),
    path('institutions/', views.institutionList, name='institution-list'),
    path('max-serial/', views.maxSerial, name='max-serial'),
    path('institutions/add', views.addInstitution, name='add-institution'),
    path('institutions/view/<int:pk>', views.viewInstitution, name='view-institution'),
    path('institutions/edit/<int:pk>', views.editInstitution, name='edit-institution'),
    path('institutions/add-next-year/<int:pk>', views.addNextYearDetails, name='add-next-year-details'),
    path('get-institutions/', views.getInstitutions, name='get-institutions'),
    path('institutions/print-list/', views.printInstitutionList, name='print-list'),

    path('institutions/settings', views.institutionSettings, name='institution-settings'),
    path('institutions/settings/add-state', views.addState, name='add-state'),
    path('institutions/settings/edit-state/<int:pk>', views.editState, name='edit-state'),

    path('institutions/settings/add-year', views.addYear, name='add-year'),
    path('institutions/settings/edit-year/<int:pk>', views.editYear, name='edit-year'),
    
    

    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
   
    # path("states/", views.state_list, name='state-list'),
    # path("years/", views.year_list, name='year-list'),
    # path("organiser/", views.organiser, name='organiser'),
    # path("institution/", views.institution, name='institution'),
    # path("ramzan-list/", views.ramzan_list, name='ramzan-list'),
    # path("state-wise-list/", views.state_wise_list, name='state-wise-list'),
    # path("list-all/", views.list_all, name='list-all'),
    # path("institute-info/<int:pk>", views.institute_info, name='institute-info'),
    # path("print-list/<ramzan_day>/<int:year>", views.print_list, name='print-list'),


]