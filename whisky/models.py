from django.db import models

class Whisky(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    abv = models.CharField(max_length=10, blank=True, null=True)
    rating = models.FloatField(default=0.0)  # 기본값을 0.0으로 설정
    price = models.FloatField()
    currency = models.CharField(max_length=10, default='USD')  # 기본값을 USD로 설정
    description = models.TextField()

    def __str__(self):
        return self.name

