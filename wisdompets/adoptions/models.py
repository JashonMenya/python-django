from django.db import models

"""
The Pet model is a subclass of django.db.models.Model.
Defines the Pet model with four fields: name, submitter, submission_date, and description.
"""


class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=1, choices=SEX_CHOICES, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    '''
    The __str__ method is a special method that returns a string representation of the object.
    '''

    def __str__(self):
        return self.name
