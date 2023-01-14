import sys
from django.shortcuts import render
import uuid
import subprocess
from django.http import JsonResponse, HttpResponse
import json
from .main_comp import main_comp_all

def main(request):
    if request.method == "GET":
        return render(request, 'backend/index.html')
    if request.method == "POST":
        codedata = request.POST['input']
        try:
            o_stdout = sys.stdout
            sys.stdout = open('file.txt','w')
            exec(codedata)
            sys.stdout.close()
            sys.stdout = o_stdout
            output = open('file.txt','r').read()
        except Exception as e:
            # sys.stdout = o_stdou
            output = e
    return render(request, 'backend/index.html',{'code':codedata,'output':output})

def main2(request):
    if request.method == "GET":
        return render(request, 'backend/index.html')
    if request.method == "POST":
        codedata = request.POST['code']
        lang = request.POST['lang']
        input_text = request.POST['input']
        # print(codedata)
        output = main_comp_all(codedata,lang,input_text)
        # context = {'output':output}
        return JsonResponse(output, safe=False)
        # return HttpResponse(json.dumps({'output':output}), content_type="application/json")