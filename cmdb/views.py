from django.shortcuts import render, redirect
from cmdb import models
USERINFO = {}


# Create your views here.
def login(request):
    # request包含用户(浏览器)提交过来的所有信息
    error_msg = ""
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
    print("跳转到index")
    bid = USERINFO.get("bid", None)
    host_list = models.Host.objects.filter(business=bid)
    return render(request,
                  'cmdb/index.html',
                  {'host_list': host_list,
                   'userinfo': USERINFO})


def insert(request):
    if request.method == "POST":
        cursor = conn.cursor()
        userid = userinfo.get("id", None)
        hostname = request.POST.get("hostname", None)
        hostip = request.POST.get("hostip", None)
        hostport = request.POST.get("hostport", None)
        department = request.POST.get("department", None)
        area = request.POST.get("area", None)
        status = request.POST.get("status", None)
        description = request.POST.get("description", None)
        sql = ("INSERT INTO cmdb_hostinfo ("
               "hostname,ip,`port`,`status`,department,area,online_time,update_time,description,user_id )"
               "VALUES ('%s','%s', %s, '%s', '%s', '%s', NOW(), NOW(), '%s', %s)" %
               (hostname, hostip, hostport, status, department, area, description, userid))
        try:
            cursor.execute(sql)
            conn.commit()
            msg = "添加成功"
            cursor.close()
        except Exception as e:
            print(e)
            msg = "系统错误"
            exit(1)
        return redirect('/index/',
                        {"msg": msg})


def detail(request):
    host_id = request.GET.get('nid')
    sql = ("SELECT	* FROM	cmdb_hostinfo WHERE `id` = %s" % host_id)
    cursor = conn.cursor()
    cursor.execute(sql)
    host = cursor.fetchone()
    return render(request,
                  'cmdb/detail.html',
                  {'host': host})


def del_host(request):
    print("del_host")
    host_id = request.POST.get('host-id')
    models.Host.objects.filter(id=host_id).delete()
    return redirect('index/',)
