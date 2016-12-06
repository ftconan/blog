# coding=utf-8

import json
from django.http import HttpResponse
from cms.models import Classification
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getClassificationList(req):
    """
    获取栏目列表
    :param req:
    :return:
    """
    classification = Classification.objects.all()
    List = []
    for obj in classification:
        classificationList = {}
        classificationList["classificationId"] = obj.classificationId
        classificationList["classificationIdLevel"] = obj.classificationIdLevel
        classificationList["classificationName"] = obj.classificationName
        classificationList["parentDirectory"] = obj.parentDirectory
        classificationList["classificationOrder"] = obj.classificationOrder
        if obj.isShow:
            classificationList["isShow"] = "是"
        else:
            classificationList["isShow"] = "否"
        List.append(classificationList)
    return HttpResponse(json.dumps(List))

@csrf_exempt
def deleteClassification(req):
    """
    删除栏目
    :param req:
    :return:
    """
    classificationId = req.POST["classificationId"]
    classification = Classification.objects.get(classificationId = classificationId)
    classification.delete()
    return HttpResponse(1)
