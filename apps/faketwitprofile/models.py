from django.contrib.auth.models import User
from django.db import models

class FaketwitProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

User.faketwitprofile = property(lambda u:FaketwitProfile.objects.get_or_create(user=u)[0])

