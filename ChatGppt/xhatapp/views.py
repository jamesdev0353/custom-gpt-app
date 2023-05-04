from django.shortcuts import render
from xhatapp.models import SaveQueries
from xhatapp.Config import BravoSis
# from datetime import datetime 
from django.utils import timezone
# Create your views here.

# initializing 
wow = BravoSis()
# wow.ai(query)

# Client for telegram
# LeosBot = Client(name="XhatGpt",api_id=wow.api_id,api_hash=wow.api_hash)

def index(request):
    return render(request, 'xhatapp/index.html')

def about(request):
    return render(request, 'xhatapp/about.html')


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