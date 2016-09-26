from django.db.models import signals
from login.models import Profile


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


signals.post_save.connect(create_profile, sender=User)
