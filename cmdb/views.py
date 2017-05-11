from django.shortcuts import render, redirect, HttpResponse
from cmdb import models
import json
USERINFO = {}


# Create your views here.
def login(request):
    # request包含用户(浏览器)提交过来的所有信息
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        obj = models.User.objects.filter(email=email, password=password).first()
        if obj:
            print("登录成功")
            global USERINFO
            USERINFO = {'id': obj.id, 'username': obj.username, 'email': obj.email, 'bid': obj.business_id}
            return redirect(index)
        else:
            error_msg = "用户名或密码错误！"
            return render(request,
                          'cmdb/login.html',
                          {"error_msg": error_msg})
    elif request.method == "GET":
        return render(request,
                      'cmdb/login.html',)
    else:
        error_msg = "请求错误！"
        return render(request,
                      'cmdb/login.html',
                      {"error_msg": error_msg})


def index(request, *args, **kwargs):
    bid = USERINFO.get("bid")  # 用户所属业务线
    host_list = models.Host.objects.filter(business=bid)
    business_list = models.Business.objects.filter(id=bid)
    if request.method == "GET":
        return render(request,
                      'cmdb/index.html',
                      {'host_list': host_list,
                       'userinfo': USERINFO,
                       'business_list': business_list})


def add_host(request):
    res = {'status': True, 'error': None, 'code': None}
    if request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        business = request.POST.get('business')
        try:
            models.Host.objects.create(hostname=hostname,
                                       ip=ip,
                                       port=port,
                                       business_id=business
                                       )
        except Exception as e:
            res['status'] = False
            res['error'] = str(e)
            print(res)
        finally:
            # return redirect('/cmdb/index/') ajax提交不能redirect, 在html对应的js中reload()
            return HttpResponse(json.dumps(res))


def del_host(request):
    if request.method == "POST":
        host_id = request.POST.get('host-id')
        models.Host.objects.filter(id=host_id).delete()
        return redirect('/cmdb/index/')


def edit_host(request):
    res = {'status': True, 'error': None, 'code': None}
    if request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        business_id = request.POST.get('business')
        hid = request.POST.get('hid')
        print(hid, hostname, ip, port, business_id)
        try:
            models.Host.objects.filter(id=hid).update(
                hostname=hostname,
                ip=ip,
                port=port,
                business_id=business_id
            )
        except Exception as e:
            res['status'] = False
            res['error'] = str(e)
            print(res)
        finally:
            # return redirect('/cmdb/index/') ajax提交不能redirect, 在html对应的js中reload()
            return HttpResponse(json.dumps(res))
