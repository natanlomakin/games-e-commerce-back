from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profilePicture = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/profile_pic')
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id']

    def __str__(self):
        return str(self._id)
