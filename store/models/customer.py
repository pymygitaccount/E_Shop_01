import email
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500) 


    # method created to save the customer inpute details.
    def register(self):       # when we use the instance method. write self as a reference variable
        self.save()
    

    @staticmethod                         # This method is created to get the specific customer by using email id.
    def get_customer_by_email(email):     # here (email) is the refrence. it dosent have any assigned values cmpaired to previous values.
        try:
            return Customer.objects.get(email = email)
        except:
            return False
 

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False




    
    