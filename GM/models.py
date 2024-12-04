from django.db import models




class Role(models.Model):
    libelle = models.CharField(max_length=20)

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False, blank=False, default='1')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    




class Materiel(models.Model):
    num_serie = models.IntegerField()
    num_inventaire = models.IntegerField(primary_key=True)
    cout = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    nombre = models.IntegerField()
    Date_Entree = models.DateField()


    class Meta:
        db_table = 'materiel'
        managed = False

    def __str__(self):
        return str(self.num_inventaire)
    

class Service(models.Model):
    id_service = models.IntegerField(primary_key=True)
    nom_service = models.CharField(max_length=100)

    class Meta:
        db_table = 'service'
        managed = False

    def __str__(self):
        return f"{self.nom_service}"
    

    

class Reclamation(models.Model):
    STATUS_CHOICES = [
        ('en_panne', 'En panne'),
    ]
    id_reclamation = models.IntegerField(primary_key=True)
    date = models.DateField()
    nom_service = models.CharField(max_length=100)
    num_bureau = models.IntegerField()
    intervention_demandee = models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_panne')

    class Meta:
        db_table = 'reclamation'
        managed = False


    def __str__(self):
        return f"{self.id_reclamation}"
    
    


class Intervention(models.Model):
    id_Intervention = models.AutoField(primary_key=True) 
    Descriptions = models.CharField(max_length=2000)
    Matériel_objet = models.CharField(max_length=1000)
    S_N = models.CharField(max_length=1000)
    Matériel_réparé = models.BooleanField()
    Matériel_réparé_non = models.TextField(blank=True, null=True)  # Allow blank or null

    class Meta:
        db_table = 'Intervention'
        managed = False

    def __str__(self):
        return f"{self.id_Intervention}"



class Bureau(models.Model):
    num_bureau = models.IntegerField(primary_key=True)
    nom_service = models.ForeignKey(Service, on_delete=models.CASCADE, db_column='nom_service')

    class Meta:
        db_table = 'bureau'
        managed = False

    def __str__(self):
        return f"{self.num_bureau}"
    



class Bureau_Materiel(models.Model):
    id = models.AutoField(primary_key=True)
    num_bureau = models.ForeignKey(Bureau, on_delete=models.CASCADE, db_column='num_bureau')
    num_inventaire = models.IntegerField()
    nombre = models.IntegerField()

    class Meta:
        db_table = 'bureau_materiel'
        managed = False
        unique_together = (('num_bureau', 'num_inventaire'))

    def __str__(self):
        return f"{self.id}"   