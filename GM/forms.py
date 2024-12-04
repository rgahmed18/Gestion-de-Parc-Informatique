from django import forms
from .models import *


class UserEmployeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'phone_number',
                  'date_of_birth', 'email', 'role']
        
class UserResponsableForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'phone_number',
                  'date_of_birth', 'email', 'role']
        


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['date', 'nom_service', 'num_bureau', 'intervention_demandee', 'status']




class MaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['num_serie', 'num_inventaire', 'cout', 'nom', 'nombre', 'Date_Entree']




class BureauForm(forms.ModelForm):
    class Meta:
        model = Bureau
        fields = ['num_bureau', 'nom_service']


class BureauMaterielForm(forms.ModelForm):
    class Meta:
        model = Bureau_Materiel
        fields = ['num_bureau', 'num_inventaire', 'nombre']




class InterventionForm(forms.ModelForm):
    class Meta:
        model = Intervention
        fields = ['Descriptions', 'Matériel_objet', 'S_N', 'Matériel_réparé', 'Matériel_réparé_non']

    def clean(self):
        cleaned_data = super().clean()
        matériel_réparé = cleaned_data.get("Matériel_réparé")
        matériel_réparé_non = cleaned_data.get("Matériel_réparé_non")
        
        if matériel_réparé:  # If repaired, no need for additional info
            cleaned_data["Matériel_réparé_non"] = ""  # Ensure it's empty
        elif not matériel_réparé and not matériel_réparé_non:
            self.add_error('Matériel_réparé_non', 'Please provide a reason if not repaired.')
        
        return cleaned_data
