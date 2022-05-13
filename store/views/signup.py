from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views import View
from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):    # used to save the
        postdata = request.POST   
        first_name = postdata.get('firstname')   # firstname & all similar fields are takem from html page.
        last_name = postdata.get('lastname')
        phone = postdata.get('userphone')
        email = postdata.get('useremail')
        password = postdata.get('userpassword') 

        # assign all customer input details to variables.
        value = {
            "first_name" : first_name,
            "last_name" : last_name,
            "phone_number" : phone,
            "Email_ID" : email
        }

        error_message = None

        customer_obj = Customer( first_name = first_name, 
            last_name = last_name, 
            phone = phone,
            email = email, 
            password = password )

        error_message = self.validateCustomer(customer_obj)

        if not error_message:
            # print(registerUser_FirstName, registerUser_LastName, registerUser_Phone, registerUser_Email, registerUser_Password)
            customer_obj.password = make_password(customer_obj.password)
            customer_obj.register()
            return redirect('homepage')    

        else:
            data = {
                "error" : error_message,
                "values" : value
            }
            return render(request, "signup.html", data)


    def validateCustomer(self, customer_obj):
        error_message = None  

        if (not customer_obj.first_name):
                error_message = "First Name Required...!"

        elif (not customer_obj.last_name): 
            error_message = "Last Name Required...!"

        elif (not customer_obj.phone):
                error_message = "Phone Number Required...!"

        elif (not customer_obj.email):
            error_message = "Email Required...!"

        elif (not customer_obj.password):
            error_message = "Password Required...!"
            
        elif len(customer_obj.password) < 3:
            error_message = "Enter the Password of 3 to 20 characters...!"

        elif customer_obj.isExists():
            error_message = "Email Address Already Registered...!"

        return error_message
