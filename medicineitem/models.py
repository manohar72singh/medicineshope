from django.db import models

# Create your models here.


class medicineRec(models.Model):
    medi_Name = models.CharField(max_length= 40)
    medi_Mfg = models.DateField()
    medi_Batch = models.CharField(max_length= 40)
    medi_Exp = models.DateField()
    medi_Comp = models.CharField(max_length=40)
    medi_Mrp = models.IntegerField()

    def __str__(self):
        return F'{self.id}--{self.medi_Name}--{self.medi_Mfg}--{self.medi_Batch}--{self.medi_Exp}--{self.medi_Comp}--{self.medi_Mrp}'



class customer(models.Model):
    cus_Name = models.CharField(max_length=50)
    cus_Email = models.CharField(max_length=100)
    cus_Mob = models.IntegerField()
    cus_Gen = models.CharField(max_length=10)
    cus_Adds = models .CharField(max_length=100)



    def __str__(self):
        return F'{self.id}--{self.cus_Name}--{self.cus_Email}--{self.cus_Mob}--{self.cus_Gen}--{self.cus_Adds}'


class Profile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}--{self.username}--{self.email}'










