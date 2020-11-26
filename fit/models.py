from django.db import models

# Create your models here.


class Patient(models.Model):
    pat_id = models.AutoField(primary_key=True)
    pat_name = models.CharField(max_length=100, default="", null=True)
    pat_phone = models.IntegerField(null=True)
    pat_email = models.CharField(max_length=100, default="", null=True)
    pat_loc = models.CharField(max_length=100, default="", null=True)
    pat_username = models.CharField(max_length=10, default="", null=True)
    pat_address = models.CharField(max_length=500, default="", null=True)

    def __str__(self):
        return self.pat_username


class Doctors(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=100, default="", null=True)
    doc_username = models.CharField(max_length=50, default="", null=True)
    doc_category = models.CharField(max_length=100, default="", null=True)
    doc_email = models.CharField(max_length=100, default="", null=True)
    doc_phone = models.IntegerField(null=True)
    doc_address = models.CharField(max_length=500, default="", null=True)
    doc_location = models.CharField(max_length=100, default="", null=True)
    doc_idProof = models.ImageField(
        upload_to='fit/doctors', default="", null=True)

    def __str__(self):
        return self.doc_username


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
    phar_name = models.CharField(max_length=100, default="", null=True)
    phar_username = models.CharField(max_length=50, default="", null=True)
    phar_ownerName = models.CharField(max_length=150, default="", null=True)
    phar_idProof = models.ImageField(
        upload_to='fit/pharmacy', default="", null=True)
    phar_StoreImage = models.ImageField(
        upload_to='fit/pharmacy', default="", null=True)
    phar_phone = models.IntegerField(null=True)
    phar_email = models.CharField(max_length=100, default="", null=True)
    phar_address = models.CharField(max_length=500, default="", null=True)
    pharmay_location = models.CharField(max_length=100, default="", null=True)

    def __str__(self):
        return self.phar_name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE, null=True)
    appointment_date = models.DateField()
    appoint_id = models.AutoField(primary_key=True)
