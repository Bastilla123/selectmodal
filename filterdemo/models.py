from django.db import models

Historie_Status_Choices = (
    (1, 'Aktiv'),
    (2, 'Inaktiv'),
)

class Historietype(models.Model):

    status = models.PositiveSmallIntegerField(choices=Historie_Status_Choices, blank=True, default=1, null=True)
    name = models.CharField(max_length=120, default="", blank=True, null=True)
    def __str__(self):
        return self.name

class Historiesubtype(models.Model):

    status = models.PositiveSmallIntegerField(choices=Historie_Status_Choices, blank=True, default=1, null=True)
    name = models.CharField(max_length=120, default="", blank=True, null=True)
    historietype_link =  models.ForeignKey(Historietype, on_delete=models.CASCADE, blank=False, null=False, default = None,
                                       )
    def __str__(self):
        return self.name

class Historiesource(models.Model):

    status = models.PositiveSmallIntegerField(choices=Historie_Status_Choices, blank=True, default=1, null=True)
    name = models.CharField(max_length=120, default="", blank=True, null=True)
    def __str__(self):
        return self.name

class Historieproperty(models.Model):

    status = models.PositiveSmallIntegerField(choices=Historie_Status_Choices, blank=True, default=1, null=True)
    name = models.CharField(max_length=120, default="", blank=True, null=True)

    def __str__(self):
        return self.name

#Example for Multiselectwidget und Singleselectwidget

class Historie(models.Model):

    historietypelink = models.ForeignKey(Historietype, on_delete=models.CASCADE, blank=True, null=True, default=None)
    historiesubtype_link = models.ForeignKey(Historiesubtype, on_delete=models.CASCADE, blank=True, null=True, default=None)
    historiesource_link = models.ManyToManyField(Historiesource,blank=True)
    historieproperty_link = models.ManyToManyField(Historieproperty,blank=True)
    historiedescription = models.TextField(default="", blank=True, null=True)
