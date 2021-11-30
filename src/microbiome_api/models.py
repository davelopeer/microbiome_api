from django.db import models

class Kingdom(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Specie(models.Model):
    label = models.CharField(max_length=500)

    def __str__(self):
        return self.label

class Entry(models.Model):
    access_id = models.CharField(max_length=500)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    sequence = models.CharField(max_length=500)

    def __str__(self):
        return self.access_id
