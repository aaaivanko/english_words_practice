from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    eng_name = models.CharField(max_length=250)
    ua_name = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ua_name} == {self.eng_name}"
