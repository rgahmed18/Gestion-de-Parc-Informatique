from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', SignIn, name='SignIn'),
    path('SignIn/', SignIn, name='SignIn'),
   
   
    path('Employe/Dashboard/', Dashboard, name='Dashboard'),
    path('Employe/Reclamation/', reclamation_view, name='Reclamation'),
    path('Employe/Suivre_Reclamation/', Suivre_Reclamation, name='Suivre_Reclamation'),
    path('SignOut/', views.EmployeSignOut, name='EmployeSignOut'),
    
    
    
    path('Responsable/Responsable_Dashboard/', Responsable_Dashboard, name='Responsable_Dashboard'),
    path('Responsable/Intervention/', Intervention_view, name='Intervention'),
    path('Responsable/Stock_Materiel/', Stock_Materiel, name='Stock_Materiel'),
    path('Responsable/Ajouter_Materiel/', Ajouter_Materiel, name='Ajouter_Materiel'),
    path('Responsable/Affecter_Materiel/', Affecter_Materiel, name='Affecter_Materiel'),
    path('Responsable/Materiel_Bureau/', Materiel_Bureau, name='Materiel_Bureau'),
    path('SignOut/', views.ResponsableSignOut, name='ResponsableSignOut'),
    # path('Admin/ActeGestion/', ActeGestion, name='ActeGestion'),
    # path('DelaiStat/DelaiStatApp/templates/Admin/tables/Departement.html', departement, name='departement'),
    # path('Admin/ActeGestion/Detail/<int:ideactge>/', ActeGestionDetail, name='ActeGestionDetail'),
    # # path('logout/', SignIn, name='logout'),
]