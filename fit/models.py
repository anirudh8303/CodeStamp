from django.db import models

# Create your models here.


class Patient(models.Model):
    pat_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=100, default="")
    pat_phone = models.IntegerField()
    pat_loc = models.CharField(max_length=100, default="")
    pat_username = models.CharField(max_length=10, default="")
    pat_address = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.pat_name


class Doctors(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=100, default="")
    doc_category = models.CharField(max_length=100, default="")
    doc_phone = models.IntegerField()
    doc_address = models.CharField(max_length=500, default="")
    doc_idProof = models.ImageField(upload_to='fit/doctors', default="")

    def __str__(self):
        return self.doc_name


class Disease(models.Model):
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doc = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True)
    disease_name = models.CharField(max_length=30, default="")
    disease_description = models.CharField(max_length=500, default="")
    med1 = models.CharField(max_length=60, default="", blank=True)
    med2 = models.CharField(max_length=60, default="", blank=True)
    med3 = models.CharField(max_length=60, default="", blank=True)
    med4 = models.CharField(max_length=60, default="", blank=True)
    med5 = models.CharField(max_length=60, default="", blank=True)
    med6 = models.CharField(max_length=60, default="", blank=True)


class Pharmacy(models.Model):
    phar_id = models.AutoField(primary_key=True)
    phar_name = models.CharField(max_length=100, default="")
    phar_ownerName = models.CharField(max_length=150, default="")
    phar_idProof = models.ImageField(upload_to='fit/pharmacy', default="")
    phar_StoreImage = models.ImageField(upload_to='fit/pharmacy', default="")
    phar_phone = models.IntegerField()
    phar_address = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.phar_name
