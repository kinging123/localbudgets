from pymongo import MongoClient
from pymongo import MongoClient as client
from django.shortcuts import render

def show_table(request, muni_name,year):
    db = client().database
    muni = db[muni_name]
    year_dataset = muni[year]
    lines = []
    for line in year_dataset.find():
        lines.append(line)

    return render(request, 'simple_table.html', {'query_results':lines} )

def index_page(request):

    res = []
    # for muni in client().database.munis.find():
        # muni['active']=''
        # res.append(muni)
    # res[0]['active']='active'
    muni = {}
    muni['id'] = 1
    muni['active'] = ''
    muni['value'] = 'ta'
    muni['heb_name'] = 'asdasd'
    res.append(muni)


    muni1 = {}
    muni1['id'] = 2
    muni1['active'] = 'active'
    muni1['value'] = 'bla'
    muni1['heb_name'] = 'dddddd'
    res.append(muni1)



    return render(request,'index.html', {'munis_result':res})
