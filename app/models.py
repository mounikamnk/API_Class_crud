from django.db import models

# Create your models here.
class Product_Categori(models.Model):
    categori_name=models.CharField(max_length=100)
    categori_id=models.PositiveIntegerField()

    def __str__(self):
        return self.categori_name
    
class Product(models.Model):
    categori_name=models.ForeignKey(Product_Categori,on_delete=models.CASCADE)
    pid=models.PositiveIntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.pname

