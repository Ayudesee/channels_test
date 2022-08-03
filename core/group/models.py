from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=32)


class GroupMembers(models.Model):
    group = models.ForeignKey("group.Group", on_delete=models.CASCADE, related_name="group_group")
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="group_user")
