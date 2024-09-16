from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile",
    )

    def __str__(self):
        return f"{self.user} profile"

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"
        db_table = "auth_user_profiles"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # Signal to create a profile for new users
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
