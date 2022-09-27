from django.shortcuts import render
from django.shortcuts import render, redirect  
from employe.forms import EmployeForm  
from employe.models import Employe 
from django.contrib import auth

# from .forms import NewUserForm
# from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from employe.functions import handle_uploaded_file  
# from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.  
def signup(request):  
    if request.method == "POST":  
        form = EmployeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employes = Employe.objects.all()  
    return render(request,"show.html",{'employes':employes})  
def edit(request, id):  
    employe = Employe.objects.get(id=id)  
    return render(request,'edit.html', {'employe':employe})  
def update(request, id):  
    employe = Employe.objects.get(id=id)  
    form = EmployeForm(request.POST, instance = employe)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employe': employe})  
def destroy(request, id):  
    employe = Employe.objects.get(id=id)  
    employe.delete()  
    return redirect("/show")  
# def login(request):  
#     if request.method == "POST":  
#         form = EmployeForm(request.POST)  
#         if form.is_valid(): 
#             form.save() 
#             return render(request,"welcome.html")
#         else:
#             return render(request,"error.html") 
#             # try:  
#             #     form.save()  
#             #     return redirect('/show')  
#             # except:  
#             #     pass  
#     else:  
#         form = EmployeForm()  
#     return render(request,'login.html')  
def login(request):
    if request.method == "POST":  
        form = EmployeForm(request.POST)  
        if form.is_valid(): 
            
            form.save() 
            return render(request,"welcome.html")
        else:
            return render(request,"error.html")
    else:
        form = EmployeForm(None)   
        return render(request,'login.html')



# def login(request):
# 	if request.method == "POST":
# 		form = EmployeForm(request.POST)
# 		if form.is_valid():
# 			ename = form.cleaned_data.get('ename')
# 			password = form.cleaned_data.get('password')
# 			employe= employe(ename=ename, password=password)
# 			if employe is not None:
# 				login(request, employe)
# 				messages.info(request, f"You are now logged in as {ename}.")
# 				return redirect("/welcome")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = EmployeForm()
# 	return render(request, 'login.html', {'form':form})

def logout(request, id): 
    if request.method == "POST":  
        auth.logout(request)
   
    return redirect("/login")  
def profile(request):
    if request.method == 'POST':
        return render(request, 'profile.html')   


def file(request):  
    if request.method == 'POST':  
        student = EmployeForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return render("File uploaded successfuly")  
    else:  
        student = EmployeForm()  
        return render(request,"index.html",{'form':form})  


