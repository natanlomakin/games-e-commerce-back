from django.db import models
from django.contrib.auth.models import User
from game.models import Game


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id','user','game']

    def __str__(self):
        return str(self._id)
