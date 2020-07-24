from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)


class City(models.Model):
    name = models.CharField(max_length=30)
    # 使用外键会自动加上后缀_id，为了避免，使用db_column字段来指定
    country = models.ForeignKey(Country, related_name='city_country', on_delete=models.CASCADE, db_column="country")
    population = models.PositiveIntegerField()