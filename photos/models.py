from django.db import models


class Images(models.Model):
    image_url = models.CharField(max_length=100, blank=False)
    image_file = models.FileField()
    user_id = models.ForeignKey(
        "auth.User", related_name="image", on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]


class Albums(models.Model):
    album_name = models.CharField(max_length=100, blank=False)
    user_id = models.ForeignKey(
        "auth.User", related_name="album", on_delete=models.CASCADE
    )
    images = models.ManyToManyField(Images)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

