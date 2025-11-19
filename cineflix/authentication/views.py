from django.shortcuts import render,redirect

from django.views import View

from .forms import LoginForm,SignUpForm

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.hashers import make_password

from cineflix.utils import generate_password

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
    

class SignUpView(View):

    template = 'authentication/signup.html'

    form_class = SignUpForm

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data = {'page' : 'Sign up','form':form}

        return render(request,'authentication/signup.html',context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.username = user.email

            password = generate_password()

            print(password)

            user.password = make_password(password)

            user.role = 'User'

            user.save()

            return redirect('login')
        
        data = {'form':form}

        return render(request,self.template)