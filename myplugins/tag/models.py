from django.db import models


# Tags are mainly used for categorizing and SEO purposes
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name
