from django.db import models


class SocialLinks(models.Model):
    platform = models.CharField(max_length=50)
    platform_url = models.URLField()

    def __str__(self):
        return self.platform
