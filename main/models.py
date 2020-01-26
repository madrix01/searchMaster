from django.db import models


class Tags(models.Model):
    tags = models.CharField(max_length=100)


    def __str__(self):
        return self.tags


class History(models.Model):
    search = models.CharField(max_length=100)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)

    def __str__(self):
        return self.search


