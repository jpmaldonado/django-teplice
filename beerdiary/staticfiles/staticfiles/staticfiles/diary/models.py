from django.db import models
from django.contrib.auth.models import User
base_char_field = models.CharField(max_length=200)

# Create your models here.
class Beer(models.Model):
    name = base_char_field
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)

    def __str__(self):
        return f"Beer Name: {self.name}"

class Entry(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        return f"Entry for {self.beer}"
        