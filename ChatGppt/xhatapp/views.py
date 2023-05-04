from django.shortcuts import render
from xhatapp.models import SaveQueries
from xhatapp.Config import BravoSis
from xhatapp.form import usserform
# from datetime import datetime 
from django.utils import timezone
# Create your views here.


###################### -login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# initializing 
wow = BravoSis()
# wow.ai(query)

# Client for telegram
# LeosBot = Client(name="XhatGpt",api_id=wow.api_id,api_hash=wow.api_hash)

def index(request):
    return render(request, 'xhatapp/index.html')

def about(request):
    return render(request, 'xhatapp/about.html')

@login_required
def query(request):
    nice = "Do you have a question you'd like me to answer?"
    result = "....."
    if request.method == 'POST':
        nice = request.POST.get('queryinput')
        print(nice)
        result = wow.ai(nice) #added new key # !--working but... Quata Exousted!
        print(result)
        # add if result is Quata Exausted later...
        # else 'ss' & 'send msg to db channel'
        ss = SaveQueries(question=nice,returnquery=result,query_time=timezone.now()) #need to check if this is working 
        ss.save()
        tim = timezone.now()
        # my_result_dict = SaveQueries.objects.order_by('-query_time')
        print(tim)
        # print(my_result_dict)
        # for data in my_result_dict:
        #     print(data.question)
        #     print(data.returnquery)
        #     print(data.query_time)
        # my_result_dict = {'query':nice,'resul':result}
# username = leo
# pass : leoleo12

    # return render(request, 'xhatapp/index.html', context=my_result_dict)
    return render(request, 'xhatapp/index.html',{'query':nice,'resul':result})


def create(request):
    acc_created = False

    if request.method == 'POST':
        usr_form = usserform(data=request.POST)

        if usr_form.is_valid():
            user = usr_form.save()
            user.set_password(user.password)
            user.save()

            acc_created = True
        else:
            print(usr_form.errors)
    
    else:
        usr_form = usserform()

    return render(request, 'xhatapp/createacc.html',{"acc_form":usr_form,"created":acc_created})


def login_usr(request):
    if request.method == 'POST':
        usrname = request.POST.get('Username')
        passwrd = request.POST.get('passsw')
        print(usrname,passwrd)

        user = authenticate(username=usrname, password=passwrd)

        if user:
            if user.is_active:
                login(request, user)
                print("checkked")
                return HttpResponseRedirect(reverse('xhat'))
          
            else:
                print("Account not usable...")
                return HttpResponse("Account not usable...")
        else:
            print(f"""
                somone tried to login!!!
                username : {usrname}
                password : {passwrd}
                """)
            return HttpResponse("OOpppzz Invalid Login Details....")
    else:
        return render(request, 'xhatapp/login.html')

@login_required
def usr_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('indexpage'))