from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from cmdb import models
# Create your views here.

# USER_INPUT = [
#     {'user':'user1','email':'email1'},
#     {'user':'user2','email':'email2'},
# ]


#处理用户请求
def index(request):
    #判断用户是否是POST请求
    if(request.method == 'POST',None):
        u = request.POST.get('user',None)
        e = request.POST.get('email',None)
        models.UserInfo.objects.create(user=u,email=e)
        #request.POST.get('pwd',None)
        # temp = {'user':user,'email':email}
        # USER_INPUT.append(temp)
        # print(user,email)
        data_list = models.UserInfo.objects.all()
    #return HttpResponse('123')
    #模板引擎
    #获取index.html模板
    return render(request,'index.html',{'data':data_list})
