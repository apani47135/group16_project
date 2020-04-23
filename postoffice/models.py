from django.db import models
from model_utils import FieldTracker
from django.utils import timezone
from django.utils.timezone import datetime



class Sender(models.Model):
    sender_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    phone_number = models.IntegerField(null=True)
    last_sent = models.DateField(null=True)

    def __str__(self):
        return self.name

class reciever(models.Model):
    reciever_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class branches(models.Model):
    branch_id = models.CharField(primary_key=True,max_length=10)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=60)
    tracker = FieldTracker()
    def __str__(self):
        return self.address


class Packages(models.Model):
    package_ID = models.IntegerField(primary_key=True)
    package_description = models.CharField(max_length=100,default="None")
    weight = models.DecimalField(max_digits=5,decimal_places=2)
    delivery_status = models.BooleanField(default=False)
    order_date = models.DateField('Date Sent')
    sent_by = models.ForeignKey(Sender,on_delete=models.CASCADE)
    sent_to = models.ForeignKey(reciever,on_delete=models.CASCADE)
    start_location=models.ForeignKey(branches,on_delete=models.CASCADE)
    tracker = FieldTracker()

    def __str(self):
        return self.package_ID


class employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=4,decimal_places=2)
    address = models.CharField(max_length=60)
    works_at = models.ForeignKey(branches,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class package_history(models.Model):
    package_ID = models.ForeignKey(Packages,on_delete=models.CASCADE)
    # current_location_id = models.ForeignKey(branches,on_delete=models.CASCADE)
    address = models.ForeignKey(branches,on_delete=models.CASCADE)
    def __str(self):
        return self.package


class location_mark(models.Model):
   package_ID = models.ForeignKey(Packages,on_delete=models.CASCADE, 
                               related_name='locations')
   current_location = models.ForeignKey(branches, on_delete=models.CASCADE)
   creation_date = models.DateTimeField(default=timezone.now, editable=False)

   def __str__(self):
      return str(self.package_ID)




