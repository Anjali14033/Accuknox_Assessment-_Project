import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item
from django.db import transaction

@receiver(post_save, sender=Item)
def item_created(sender, instance, **kwargs):
    print("Signal Thread:", threading.get_ident())
    print("In transaction block:", transaction.get_connection().in_atomic_block)
