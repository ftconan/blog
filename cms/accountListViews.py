# coding=utf-8

import json
from django.http import HttpResponse
from cms.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getAccountList(req):
    """
    获取账号列表
    :param req:
    :return:
    """
    account = User.objects.all()
    List = []
    for obj in account:
        accountList = {}
        accountList["userId"] = obj.userId
        accountList["userName"] = obj.userName
        accountList["userAccount"] = obj.userAccount
        accountList["password"] = obj.password
        accountList["isShow"] = obj.isShow
        if obj.isShow:
            accountList["isShow"] = "是"
        else:
            accountList["isShow"] = "否"
        List.append(accountList)
    return HttpResponse(json.dumps(List))

@csrf_exempt
def deleteAccount(req):
    """
    删除账号
    :param req:
    :return:
    """
    userId = req.POST["userId"]
    account = User.objects.get(userId = userId)
    account.delete()
    return HttpResponse(1)

@csrf_exempt
def getUserName(req):
    """
    通过cookie中管理员id 获取用户的帐号
    :param req:
    :return:
    """
    userId = req.COOKIES.get('userId','')
    userList = {}
    userAccount = User.objects.get(userId=userId)
    userList["userAccount"] = userAccount.userAccount
    return HttpResponse(userAccount["userAccount"])
