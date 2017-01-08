# coding:utf-8

from django.views.decorators.csrf import csrf_exempt
from models import User
import os
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response


@csrf_exempt
def login(req):
    """
    管理员登录
    :param req:
    :return:
    """
    if req.method == 'POST':
        userAccount = req.POST["account"]
        password = req.POST["password"]
        userForm = [userAccount, password]
        user = User.objects.filter(userAccount=userAccount)
        if userForm != "":
            if user.count() == 0:
                return HttpResponse("<script type='text/javascript'>alert('用户名不存在');window.location.href='login';</script>")
            if user[0].password != password:
                return HttpResponse(
                    "<script type='text/javascript'>alert('用户名或密码错误');window.location.href='login';</script>")
            else:
                # 如果是普通用户，跳转到首页
                if user[0].state == 2:
                    response = HttpResponseRedirect("/client")
                    userId = user[0].userId
                    # 将userId写入浏览器cookies
                    return response
                else:
                    response = HttpResponseRedirect("newsList")
                    userId = user[0].userId
                    # 将userId写入浏览器cookies
                    response.set_cookie('userId', userId)
                    return response
        else:
            return HttpResponse("<script type='text/javascript'>alert('用户名或密码不能为空');window.location.href='login';</script>")
    else:
        return render_to_response("login.html")


def logout(req):
	"""
	管理员退出
	:param req:
	:return:
	"""
	response = HttpResponse("<script type='text/javascript'>alert('管理员退出');window.location.href='login'</script>")
	#清理cookie里保存userName
	response.delete_cookie('userId')
	return response

def judgeadmin(test):
    """
    判断是否登录，后台操作的全局判断，用作装饰器
    :param test:
    :return:
    """
    def infun(req, *args, **kwargs):
        if req.COOKIES.get('userId','') == '':
            return HttpResponseRedirect('login')
        else:
            userId = User.objects.filter(userId=req.COOKIES.get('userId',''))
            if userId.count() == 0:
                return HttpResponse("<script type='text/javascript'>alert('该用户不存在');window.location.href='login';</script>")
            else:
                ret=test(req, *args, **kwargs)
                return ret
    return infun

def adminskip(func):
    """
    跳转异常装饰器
    """
    def infun(req, *args, **kwargs):
        basePath=os.path.dirname(os.path.dirname(__file__))
        logPath=os.path.join(basePath,"cms/log/skip.txt")
        log_file = open(logPath,"a")
        try:
            ret=func(req, *args, **kwargs)
        except Exception as err:
            log_file.writelines(str(time.strftime('%Y/%m/%d %H:%M:%S'))+"\tview:"+func.__name__+"\nerror:["+str(err)+"]\ndoc:"+func.__doc__+"\n")
            return render_to_response('404.html')
        finally:
            log_file.close()
        return ret
    return infun

def adminselect(func):
    """
    查找异常装饰器
    """
    def infun(req, *args, **kwargs):
        basePath=os.path.dirname(os.path.dirname(__file__))
        logPath=os.path.join(basePath,"cms/log/select.txt")
        log_file=open(logPath,"a")
        try:
            ret=func(req, *args, **kwargs)
        except Exception as err:
            log_file.writelines(str(time.strftime('%Y/%m/%d %H:%M:%S'))+"\tview:"+func.__name__+"\nerror:["+str(err)+"]\ndoc:"+func.__doc__+"\n")
            return render_to_response('404.html')
        finally:
            log_file.close()
        return ret
    return infun


def adminupdate(func):
    """
    增删改异常装饰器
    """
    def infun(req, *args, **kwargs):
        basePath=os.path.dirname(os.path.dirname(__file__))
        logPath=os.path.join(basePath,"cms/log/update.txt")
        log_file=open(logPath,"a")
        try:
            ret=func(req, *args, **kwargs)
        except Exception as err:
            log_file.writelines(str(time.strftime('%Y/%m/%d %H:%M:%S'))+"\tview:" + func.__name__+"\nerror:["+str(err) + "]\ndoc:"+func.__doc__+"\n")
            return render_to_response('404.html')
        finally:
            log_file.close()
        return ret
    return infun
