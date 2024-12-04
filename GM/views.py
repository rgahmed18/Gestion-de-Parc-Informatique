from django.shortcuts import render, redirect
from django.http import JsonResponse    
from django.core.serializers import serialize
from .forms import *
from .models import *



id_Responsable_role = 1
id_Employe_role = 2

def SignIn(request):
    if request.method == "GET":
        return render(request, 'SignIn.html')
    elif request.method == "POST":

        user = User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).first()
        
        if user is None:
            return JsonResponse({'status': 'error', 'message' : 'Incorrect username or password'})

        user.password = "NICE_TRY"
        user.role.libelle = user.role.libelle[0]

        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'phone_number': user.phone_number,
            'date_of_birth': user.date_of_birth,
            'email': user.email,
            'role': user.role.libelle,
        }

        request.session['USER_ID'] = user.id

        if user.role.libelle == "RESPONSABLE"[0]:
            print("DEBUG RESPONSABLE")
            return JsonResponse({'status': 'success', 'message' : 'Signed in successfully', 'user' : user_data})
        elif user.role.libelle == "EMPLOYE"[0]:
            print("DEBUG EMPLOYE")
            return JsonResponse({'status': 'success', 'message' : 'Signed in successfully', 'user' : user_data})
        else:
            return JsonResponse({'status': 'error', 'error' : 'Unrecognized User Role'})
        



def Dashboard(request):
    if request.method == "GET":
        user_id = request.session.get('USER_ID')

        user = User.objects.filter(id=user_id).first()
        
        if user is None:
            return redirect('SignIn')

        if user.role.id != id_Employe_role:
            return redirect('SignIn')
        
        return render(request, 'Employe/Dashboard.html', {
            'user': user,
        })

    

def reclamation_view(request):
    if request.method == 'POST':
        user_id = request.session.get('USER_ID')

        user = User.objects.filter(id=user_id).first()
        form = ReclamationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Reclamation', {'user': user})
    else:
        form = ReclamationForm()
        results = Reclamation.objects.all()
    return render(request, 'Employe/Reclamation.html', {'form': form, 'results': results,})
    


def Suivre_Reclamation(request):
    if request.method == "GET":
        print("PAGE GET")
        results = Reclamation.objects.all()
        return render(request, "Employe/Suivre_Reclamation.html", {'results': results})
    elif request.method == "POST":
        print("POST DATA")
        return render(request, "Employe/Suivre_Reclamation.html")
    


def EmployeSignOut(request):
    if request.method == "GET":
        user_id = request.session.get('USER_ID')

        if user_id is None:
            return redirect('SignIn')

        user = User.objects.filter(id=user_id).first()
        
        if user is None or user.role.id != id_Employe_role:
            return redirect('SignIn')

        request.session.flush()  # Clears all session data

        return redirect('SignIn')
    







def Responsable_Dashboard(request):
    if request.method == "GET":
        user_id = request.session.get('USER_ID')

        user = User.objects.filter(id=user_id).first()
        
        
        reclamations = Reclamation.objects.all()
        results = Intervention.objects.all()
        for r in results:
            r.Matériel_réparé = int.from_bytes(r.Matériel_réparé)
        return render(request, "Responsable/Responsable_Dashboard.html", {'results': results, 'reclamations' : reclamations})

    elif request.method == "POST":
        print("POST DATA")
        return render(request, "Responsable/Responsablee_Dashboard.html")
    

    
def Intervention_view(request):
    if request.method == 'POST':
        form = InterventionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Intervention')
    else:
        form = InterventionForm()
    return render(request, 'Responsable/Intervention.html', {'form': form})


def Ajouter_Materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ajouter_Materiel')
    else:
        form = MaterielForm()
    return render(request, 'Responsable/Ajouter_Materiel.html', {'form': form})


def Stock_Materiel(request):
    if request.method == "GET":
        print("PAGE GET")
        results = Materiel.objects.all()
        return render(request, "Responsable/Stock_Materiel.html", {'results': results})
    elif request.method == "POST":
        print("POST DATA")
        return render(request, "Responsable/Stock_Materiel.html")
    



def Affecter_Materiel(request):
    services = Service.objects.all()
    stocks = Materiel.objects.all()
    bureaux = Bureau.objects.all()

    if request.method == 'POST':
        form = BureauMaterielForm(request.POST)
        if form.is_valid():
  
            bureau_materiel = form.save()


            num_inventaire = form.cleaned_data['num_inventaire']
            nombre_to_assign = form.cleaned_data['nombre']
            materiel = Materiel.objects.get(num_inventaire=num_inventaire)
            

            if materiel.nombre >= nombre_to_assign:
                materiel.nombre -= nombre_to_assign
                
                if materiel.nombre == 0:
                    materiel.delete()
                materiel.save()


            return redirect('Affecter_Materiel')
    else:
        form = BureauMaterielForm()

    return render(request, 'Responsable/Affecter_Materiel.html', {'form': form, 'services': services, 'stocks': stocks, 'bureaux': bureaux})







def Materiel_Bureau(request):
    if request.method == "GET":
        print("PAGE GET")
        bureau_materiels = Bureau_Materiel.objects.all()
        return render(request, "Responsable/Materiel_Bureau.html", {'bureau_materiels': bureau_materiels})
    elif request.method == "POST":
        print("POST DATA")
        return render(request, "Responsable/Materiel_Bureau.html")
    

def ResponsableSignOut(request):
    if request.method == "GET":
        user_id = request.session.get('USER_ID')

        if user_id is None:
            return redirect('SignIn')

        user = User.objects.filter(id=user_id).first()
        
        if user is None or user.role.id != id_Responsable_role:
            return redirect('SignIn')

        request.session.flush()  # Clears all session data

        return redirect('SignIn')


def Roles(request):
    if request.method == "GET":
        roles = User.objects.all()
        roles_json = serialize('json', roles)
        return JsonResponse(roles_json, safe=False)