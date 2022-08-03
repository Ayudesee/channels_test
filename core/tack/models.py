from django.db import models


class Tack(models.Model):
    tacker = models.ForeignKey("user.User", on_delete=models.CASCADE)
    group = models.ForeignKey("group.Group", on_delete=models.CASCADE)
    price = models.IntegerField()
    name = models.CharField(max_length=16)
