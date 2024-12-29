from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Reader


@receiver(post_save, sender=User)
def create_reader(sender, instance, created, **kwargs):
    """
    Automatically create a Reader object when a User is created.
    """
    if created:  # Check if the User object is created for the first time
        phone_number = getattr(instance, '_phone_number', None)
        Reader.objects.create(user=instance, phone_number=phone_number)
        print("User created")


@receiver(post_save, sender=User)
def save_reader(sender, instance, **kwargs):
    """
    Save the related Reader object when the User is saved.
    """
    if hasattr(instance, 'reader'):  # Check if the Reader object exists
        print('reader created --> saving....')
        instance.reader.save()
    else:
        print('reader was NOT created')
