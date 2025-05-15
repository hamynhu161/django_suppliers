from django.db import models

class Supplier(models.Model):
    companyName = models.CharField(max_length=50, default="firma")
    contactName = models.CharField(max_length=50, default="firma")
    address = models.CharField(max_length=100, default="firma")
    phone = models.CharField(max_length=20, default="firma")
    email = models.CharField(max_length=50, default="firma")
    country = models.CharField(max_length=50, default="firma")
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):          #show this text (ABC company example) instead of a generic name like <Supplier: Supplier object (1)>
        return f"{self.companyName} from {self.country}"

class Product(models.Model):
    productName = models.CharField(max_length=20, default="laku")
    packagesize = models.CharField(max_length=20, default=3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default=3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)    #on_delete...:If the supplier is deleted, all their products will also be deleted.
    # ao:n voi tehdä jos haluaa että admin sivu toimii myöhemmässä vaiheessa paremmin,
    # mutta se ei ole välttämätöntä alussa
    def __str__(self):
        return f"{self.productName} produced by {self.supplier.companyName}"