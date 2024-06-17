from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Password(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.password
