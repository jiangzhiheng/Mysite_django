from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

#处理用户请求
def index(request):
    #return HttpResponse('123')
    return render(request,'index.html')
