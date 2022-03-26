from django.shortcuts import render
from  .models import Production
import pandas as pd
import sqlite3

# Create your views here.

annual = Production()

def index(request):
	return render(request, 'index.html')

def calculate(request):
    api_number = int(request.GET['well'])
    df = pd.read_excel('ohio/production.xls')
    total_api = set(df['API WELL NUMBER'])
    if api_number not in total_api:
        raise Exception("Sorry, API WELL NUMBER is invalid!")
    else:
        pass
    annual.api_well_number = api_number
    annual.oil = 0
    for i in range(4):
        annual.oil += df.loc[(df['API WELL NUMBER'] == api_number)]['OIL'].values[i]

    annual.gas = 0
    for i in range(4):
        annual.gas += df.loc[(df['API WELL NUMBER'] == api_number)]['GAS'].values[i]

    annual.brine = 0
    for i in range(4):
        annual.brine += df.loc[(df['API WELL NUMBER'] == api_number)]['BRINE'].values[i]
    return render(request, 'index.html', {"annual": annual, "api_number": api_number})

def insert(request):
    annual.save()
    find_data = Production.objects.get(api_well_number=annual.api_well_number)
    return render(request, 'index.html', {"data": find_data, "api_number": find_data.api_well_number})
