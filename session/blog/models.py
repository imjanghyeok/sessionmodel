from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=10,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    introduce = models.TextField()
    sns_id = models.URLField(max_length=200)
    age_list = []
    for i in range(0,100):
        age_list.append((i, 1930+i))
    age = models.IntegerField(choices=age_list, default="0")
    email = models.EmailField(max_length=30)
    modify_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title