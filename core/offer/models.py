from django.db import models


class Offer(models.Model):
    tack = models.ForeignKey("tack.Tack", on_delete=models.CASCADE)
