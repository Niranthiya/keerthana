from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    code_no = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    email_id = models.CharField(max_length=45)
    contact_no = models.CharField(max_length=10)
    class Meta:
        db_table="EmpDetails"








