from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    peoples=[
        {'name':'abijett','age':26},
        {'name':'deep','age':28},
        {'name': 'de', 'age': 21},
        {'name': 'vickey', 'age': 29},
    ]
    vegetables=['potao','tomato','ladyfinger']
    for peoples in peoples:
        print(peoples)
    return render(request,"home/index.html",context={ 'peoples':peoples,'vegetables':vegetables})



def success_page(request):
    print("*",10)
    return HttpResponse("<h1> this is success page </h1>")
def about(request):
    print("*",10)
    return HttpResponse("<h1> this is sabout page </h1>")
def contact(request):
    print("*",10)
    return HttpResponse("<h1> this is contact page </h1>")


