from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Userinfo
import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
import urllib
from .json import DateEncoder
import time
import datetime
# from .public_data import Normal_Flag
normal_flag = 1
openid = ""
# access_token = ''


# 配置微信
# django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    global openid
    try:
        if request.method == "GET":
            createMenu()
            print("222")
            # 接收微信服务器get请求发过来的参数
            signature = request.GET.get('signature', None)
            timestamp = request.GET.get('timestamp', None)
            nonce = request.GET.get('nonce', None)
            echostr = request.GET.get('echostr', None)
            # 服务器配置中的token
            token = 'abc'
            # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
            hashlist = [token, timestamp, nonce]
            hashlist.sort()
            hashstr = ''.join([s for s in hashlist])
            # hashstr = hashlib.sha1(hashstr).hexdigest()
            hashcode = hashlib.sha1(hashstr.encode('utf-8')).hexdigest()
            if hashcode == signature:
                print("333")
                return HttpResponse(echostr)
            else:
                return HttpResponse("配置失败")
        else:
            # othercontent = autoreply(request)
            openid = request.GET.get('openid', None)
            print("----openid-----")
            return HttpResponse("othercontent")

    except Exception as e:
        return e

# 获取accesstoken


def getToken():
    print("获取token")
    appid = "wx827f74d01d56c54f"
    secret = "953ee7241d6d2e0720a330cf44f24b2a"
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
        appid, secret)
    print(url)
    # urlopen表示打开一个网页获取所有内容
    result = urllib.request.urlopen(url).read()
    access_token = json.loads(result).get('access_token')
    print('access_token===%s' % access_token)
    return access_token
    # return HttpResponse(result)


def createMenu():
    access_token = getToken()
    print("开始创建菜单")
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % access_token
    print(url)
    data = {
        "button": [
            # {
            #     "name": "菜单1",
            #     "sub_button": [
            #         {
            #             "type": "click",
            #             "name": "子菜单1",
            #             "key": "meitu"
            #         },
            #         {
            #             "type": "view",
            #             "name": "子菜单2",
            #             "url": "http://dnwvsa.natappfree.cc/admin/"
            #         }]
            # },
            {
                "type": "view",
                "name": "再次上报",
                "url": "http://testwechat.vipgz2.idcfengye.com/retable/"
            },
            {
                "type": "view",
                "name": "填报信息",
                "url": "http://testwechat.vipgz2.idcfengye.com/table/"

            }

        ]
    }
    # loads方法是把json对象转化为python对象，dumps方法是把pyhon对象转化为json对象
    #data = json.loads(data)
    #data = urllib.urlencode(data)
    # 构造一个Request对象
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('encoding', 'utf-8')
    response = urllib.request.urlopen(
        req, bytes(json.dumps(data, ensure_ascii=False), encoding="utf8"))
    result = response.read()
    # return result
    return HttpResponse(result)


# 获取数据库中的所有观影人员信息
def userinfo(request):
    # 去model里取数据
    userlist = list(Userinfo.objects.all().values())
    # userlist.append(Userinfo.objects.all())
    # print(type(userlist))
    # print(userlist)
    # 将数据传递给模板,以供模板再渲染页面，将渲染好的页面返回给浏览器
    return HttpResponse(json.dumps(userlist, cls=DateEncoder, ensure_ascii=False))
    # return render(request, 'myAPP/userinfo.html', {"userinfos": userlist})


# 获取异常人员信息
def getUnNormalUser(request):
    # 去model里取数据
    userlist = list(Userinfo.objects.filter(isnormal=0).values())
    print("--------异常人员--------")
    print(userlist)
    return HttpResponse(json.dumps(userlist, cls=DateEncoder, ensure_ascii=False))
    # return render(request, 'myAPP/userinfo.html', {"userinfos": userlist})


# 获取填报表单
def table(request):
    return render(request, 'table.html')


# 再次获取填报表单,该表单自动加载已填写的信息
def retable(request):
    global openid
    try:
        user = Userinfo.objects.get(openid=openid)
        userinfo = {}
        userinfo["uname"] = user.uname
        userinfo["ic_number"] = user.ic_number
        userinfo["tel_number"] = user.tel_number
        userinfo["room"] = user.room
        userinfo["seat"] = user.seat
        userinfo["temperature"] = user.temperature

        return render(request, 'retable.html', {"userinfo": userinfo})
    except Userinfo.DoesNotExist:
        return HttpResponse("获取失败，请确认是否已经填报过信息！")
     # return render(request, 'myAPP/userinfo.html', {"userinfos": userlist})


# 提交表单处理
def submit(request):
    # print(request.POST.get('signature', None))
    global normal_flag
    global openid
    # emptyCheck=['uname','ic_number','tel_number','room','seat','temperature']
    # for etpye in emptyCheck:
    #     if(len(request.POST[etpye])==0):
    #         return HttpResponse("请填好完整信息！")

    if (float(request.POST['temperature']) > 37.0):
        normal_flag = 0

    # 查看是否是第一次提交
    try:
        user = Userinfo.objects.get(uname=request.POST['uname'])
        user.isnormal = normal_flag
        user.temperature = float(request.POST['temperature'])
        user.save()
    except Userinfo.DoesNotExist:
        new_user = Userinfo()
        new_user.uname = request.POST['uname']
        new_user.ic_number = request.POST['ic_number']
        new_user.tel_number = request.POST['tel_number']
        new_user.room = request.POST['room']
        new_user.seat = request.POST['seat']
        new_user.temperature = float(request.POST['temperature'])
        new_user.date = datetime.datetime.now()
        new_user.isnormal = normal_flag
        # new_user.openid = openid
        new_user.openid ='12345wertyxcv456'
        new_user.save()

    return render(request, 'success.html')


# 轮询监测查看normal_flag
def monitor(request):
    global normal_flag
    print(normal_flag)
    if (normal_flag == 0):
        normal_flag = 1
        return HttpResponse(normal_flag-1)
    else:
        return HttpResponse(normal_flag)


# 给根据openid给特定的微信用户发送消息
def sendMessage(request):
    global openid
    access_token = getToken()
    openid = request.GET.get("openid")
    print("给指定用户发送消息")
    url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s" % access_token
    # print(url)
    data = {
        "touser": openid,
        "msgtype": "text",
        "text":
        {
            "content": "提醒：您所在的电影厅出现体温异常人员，请您注意！"
        }
    }
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('encoding', 'utf-8')
    response = urllib.request.urlopen(
        req, bytes(json.dumps(data, ensure_ascii=False), encoding="utf8"))
    result = response.read()
    return HttpResponse(result)

# def warnUser(request,list ):
