from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from store.models.category import Category
from store.models.customer import Customer
from store.models.product import Product


class Login(View):        # class based view
    return_url = None 
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        login_email = request.POST.get('useremail')
        login_password = request.POST.get('userpassword')
        customer = Customer.get_customer_by_email(login_email)
        error_message = None
        if customer:
            flag = check_password(login_password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect("homepage")
            else:
                error_message = "Email or Password Invalid...!"
        else:    
            error_message = "Email or Password Invalid...!"
        print( login_email, login_password )
        return render(request, 'login.html' , {"error" : error_message})


def logout(request):
    request.session.clear()
    return redirect('login')