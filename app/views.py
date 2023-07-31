from django.shortcuts import render

# Create your views here.
def CDT(request):
    d = {'name' :'anji','age':20,'hobbies':['cricket','football']}
    return render(request,'for loop.html',context=d)