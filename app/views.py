from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.forms import MyForm
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from app.models import Employee
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='login')
def Home(request, id=0):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        if request.method == "GET":
           if id == 0:
                form = MyForm()
           else:
                employee = Employee.objects.get(pk=id)
                form = MyForm(instance=employee)
           return render(request, "add.html", {'form': form})
        else:
           if id == 0:
                form = MyForm(request.POST)
           else:
                employee = Employee.objects.get(pk=id)
                form = MyForm(request.POST,instance= employee)
           if form.is_valid():
                form.save()
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                print(todo)
           return redirect('read')



def Login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )


def Signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)
        
def Signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def Read(request):
    if request.user.is_authenticated:
        user = request.user
        emp = Employee.objects.filter(user = user)
        paginator = Paginator(emp,6)
        page_number = request.GET.get('page')
        empfinal = paginator.get_page(page_number)
        last = empfinal.paginator.num_pages
        total = empfinal.paginator.count
    
        context = {
            'emp': empfinal,
            'last': last,
            'total': total,
            'pagelist' : [n+1 for n in range(last)],
        }
        return render(request, 'read.html', context)
    

def delete(request , id):
    print(id)
    Employee.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('read'))


@login_required(login_url='login')
def Search(request):
    if request.user.is_authenticated:
        user = request.user
        emp0 = Employee.objects.filter(user = user)
        query = request.GET['query']
        emp1 = emp0.filter(name__icontains=query)
        emp2 = emp0.filter(myid__icontains=query)
        emp3 = emp0.filter(email__icontains=query)
        emp = emp1.union(emp2,emp3)
        paginator = Paginator(emp,100)
        page_number = request.GET.get('page')
        empfinal = paginator.get_page(page_number)
        last = empfinal.paginator.num_pages
        total = empfinal.paginator.count
    
        context = {
            'emp': empfinal,
            'last': last,
            'total': total,
            'pagelist' : [n+1 for n in range(last)],
            'query':query,
        }
        return render(request, 'search.html', context)
    

    
    