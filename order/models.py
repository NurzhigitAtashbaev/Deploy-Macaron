from django.db import models


class Table(models.Model):
    number = models.IntegerField()
    seats = models.IntegerField()
    busy = models.BooleanField(default=False)

    visitor_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True, max_length=2000)
    start_time = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.number} {self.busy} {self.visitor_name}'

