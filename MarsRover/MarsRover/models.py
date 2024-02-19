from django.db import models

class Rover(models.Model):
    planet = models.ForeignKey('Planet', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    orientation_choices = (
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West'),
    )
    orientation = models.CharField(max_length=1, choices=orientation_choices)
