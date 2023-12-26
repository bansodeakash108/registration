from django.db import models

# Create your models here.


class api_model(models.Model):
    cust_id=models.AutoField(primary_key=True)
    cust_name=models.CharField(max_length=50)
    cust_details=models.TextField()