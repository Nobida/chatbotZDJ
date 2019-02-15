# -*- coding: utf-8 -*-

from django.http import HttpResponse
import json
import os
import sys
cur_path = os.getcwd()+'/ZDJ'
sys.path.append(cur_path)
from QA.MainProgram import run
from QA.Py2Neo import keywords,path,net

 
# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            query = request.POST.get('query', 0)
            if query:
                res = run(query)
                dic['res'] = res
                dic = json.dumps(dic,ensure_ascii=False)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')

def related(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            entity = request.POST.get('entity', 0)
            if entity:
                res = keywords(entity)
                dic['res'] = res
                dic = json.dumps(dic,ensure_ascii=False)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')

def shortestpath(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            entity1 = request.POST.get('entity1', 0)
            entity2 = request.POST.get('entity2', 0)
            if entity1 and entity2:
                res = path(entity1,entity2)
                res = [str(i) for i in res]
                dic['res'] = res
                dic = json.dumps(dic,ensure_ascii=False)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')

def network(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            entity = request.POST.get('entity')
            lim_num = request.POST.get('lim_num')
            if entity and lim_num:
                res = net(entity,lim_num)
                res = [str(i) for i in res]
                dic['res'] = res
                dic = json.dumps(dic,ensure_ascii=False)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')

