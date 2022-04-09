from django.db import models

class Unit_Type(models.Model):
    unit_name = models.CharField(max_length=50)

    def __str__(self):
        return self.unit_name