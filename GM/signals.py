# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Bureau_Materiel, Materiel

# @receiver(post_save, sender=Bureau_Materiel)
# def delete_from_stock(sender, instance, **kwargs):
#     materiel = instance.num_inventaire
#     materiel.delete()
