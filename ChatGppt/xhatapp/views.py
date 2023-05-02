from django.shortcuts import render
from xhatapp.models import SaveQueries
from xhatapp.Config import BravoSis

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
    if request.method == 'POST':
        nice = request.POST.get('queryinput')
        print(nice)
        result = wow.ai(nice) # working but... Quata Exousted!
        print(result)
        # add if result is Quata Exausted
        # else 'ss' & 'send msg to db channel'
        ss = SaveQueries(nice,result) #need to check if this is working 
        ss.save()




    return render(request, 'xhatapp/index.html')