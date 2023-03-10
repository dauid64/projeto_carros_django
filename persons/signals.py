from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cars.models import Person


@receiver(post_save, sender=User)
def create_person(sender, instance, created, *args, **kwargs):
    if created:
        person = Person.objects.create(
            author=instance
        )
        person.save()
