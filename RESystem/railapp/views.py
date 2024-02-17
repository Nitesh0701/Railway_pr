import json
import requests
import pandas as pd


from django.shortcuts import render

my_dict={'rail_1':"this page gives info",}

# Create your views here.
from django.http import HttpResponse,JsonResponse



from railapp.train_service.get_trains import get_trains

def index(request):
         #return HttpResponse(" Hello this is my first Django App")
		 return HttpResponse("<h2> I am rendering from apps view </h2>")


"""def train_search_view(req):
    response =get_trains('TLGP','SBC','2024-02-12')
    json_response =response

    json_data=json_response

    extracted_data=[]
    for train in json_data['data']:
        extracted_data.append({
            'train_number': train['train_number'],
            'train_name': train['train_name'],
            'run_days': ', '.join(train['run_days']),
            'train_src': train['train_src'],
            'train_dstn': train['train_dstn'],
            'from_std': train['from_std'],
            'to_std': train['to_std'],
        })


    return render(req,'railapp/my_template.html',{'extracted_data':extracted_data})"""

def train_search_view_org(req):
    response = get_trains('TLGP','SBC','2023-07-12')

    return JsonResponse(response)

def train_search_view(req):
    response = get_trains('TLGP','SBC','2024-02-20')
    daata= response['data']
    df=pd.DataFrame(daata)
    html_table=df
    return render(req,'railapp/train_search.html',{'html_table':html_table})

def getTrains(request):
    return render(request,'login.html',context=my_dict)

def railinfo(request):
    return render(request,'rail_info.html')

def index1(request):
    return render(request,'search.html')

def index2(request):
    return render(request,'pnr.html')