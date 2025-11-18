from django.shortcuts import render,redirect

from django.views import View

from .forms import LoginForm

from django.contrib.auth import authenticate,login,logout

# Create your views here.

class LoginView(View):

    template = 'authentication/login.html'

    form_class = LoginForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'form':form}

        return render(request,self.template,context=data)
    


    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        error = None

        if form.is_valid():

            email = form.cleaned_data.get('email')

            password = form.cleaned_data.get('password')

            user = authenticate(username=email,password=password)

            if user:

                login(request,user)

                return redirect('home')
            
            error = 'Invalid username or password'
    
        data = {'form' :form,'error':error}

        return render(request,self.template,context=data)


class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect('home')
    
