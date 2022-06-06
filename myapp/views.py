from django.shortcuts import render  
import datetime  
# Create your views here.  
from django.http import HttpResponse  
from django.http import HttpResponse, HttpResponseNotFound 
from django.views.decorators.http import require_http_methods 
from myapp.functions.functions import handle_uploaded_file
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
#from myapp.form import EmployeeForm 
from myapp.form import StudentForm 
from myapp.models import Employee
import csv  
from reportlab.pdfgen import canvas
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django Framework!</h2>")  

 
#def index(request):  
#    now = datetime.datetime.now()  
#    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
#   return HttpResponse(html)    # rendering the template in HttpResponse 

#def index(request):  
#   a = 1  
#   if a:  
#        return HttpResponseNotFound('<h1>Page not found</h1>')  
#   else:  
#        return HttpResponse('<h1>Page was found</h1>') # rendering the template in HttpResponse

@require_http_methods(["GET"])  
def show(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')

#def index(request):  
#   template = loader.get_template('index.html') # getting our template  
#   return HttpResponse(template.render()) 

#def index(request):  
#   template = loader.get_template('index.html') # getting our template  
#   name = {  
#        'student':'nandhini'  
#    }  
#    return HttpResponse(template.render(name))       # rendering the template in HttpResponse   

@require_http_methods(["GET"])    
def hello(request):    
    return HttpResponse('<h1>This is Http GET request.</h1>')

#def index(request):  
#    return render(request,'index.html')  

#def index(request):  
#    stu = EmpForm()  
#    return render(request,"index.html",{'form':stu})

#def index(request):  
#    student = StudentForm()  
#    return render(request,"index.html",{'form':student}) 

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  


def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})


def methodinfo(request):  
    return HttpResponse("Http request is: "+request.method)


def getdata(request):  
    try:  
        data = Employee.objects.get(id=12)  
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
        return HttpResponse(data);  

def setsession(request):  
    request.session['sname'] = 'irfan'  
    request.session['semail'] = 'irfan.sssit@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['sname']  
    studentemail = request.session['semail']  
    return HttpResponse(studentname+" "+studentemail);  

def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('django-tutorial', 'django.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['django-tutorial']  
    return HttpResponse("django tutorials @: "+  tutorial);

def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response

# def getfile(request):  
#     response = HttpResponse(content_type='text/csv')  
#     response['Content-Disposition'] = 'attachment; filename="file.csv"'  
#     employees = Employee.objects.all()  
#     writer = csv.writer(response)  
#     for employee in employees:  
#         writer.writerow([employee.eid,employee.ename,employee.econtact])  
#     return response  

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Everyone.")  
    p.showPage()  
    p.save()  
    return response  
