import uuid
import subprocess
import os
from django.conf import settings

d_file=str(settings.DATA_OUT_FILES)
b_dir = str(settings.BASE_DIR)

def main_comp_all(codedata,lang,input_text):
    try:
        file_name = str(uuid.uuid4())
        with open(d_file+"/codes/"+lang+"/" + file_name+'.'+lang,'w') as f:
            f.write(codedata)
        if lang=="py":
            if input_text:
                result = subprocess.run([str(settings.PATH_PYTHON),"data_out/codes/py/"+file_name+'.'+lang], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
            else:
                result = subprocess.run([str(settings.PATH_PYTHON),"data_out/codes/py/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if lang=="js":
            result = subprocess.run(["node","data_out/codes/js/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if lang=="cpp":
            result = subprocess.run(["g++","data_out/codes/cpp/"+file_name+'.'+lang,"-o","data_out/codes/cpp/"+file_name+"_exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                result = subprocess.run(["data_out/codes/cpp/"+file_name+"_exe"], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="c":
            result = subprocess.run(["gcc","data_out/codes/c/"+file_name+'.'+lang,"-o","data_out/codes/c/"+file_name+"_exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                result = subprocess.run(["data_out/codes/c/"+file_name+"_exe"], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="php":
            result = subprocess.run(["C:/xampp/php/windowsXamppPhp/php.exe","data_out/codes/php/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        if result.returncode == 0:
            data = {'output':result.stdout.decode("utf-8"),'type':"success"}
        else:
            out = result.stderr.decode("utf-8")
            out = out.replace("data_out/codes/"+lang+"/"+file_name+'.'+lang,"main."+lang)
            out = out.replace("D:\\Django\\nvscompiler\\Code\\data_out\\codes\\"+lang+"\\"+file_name+'.'+lang,"main."+lang)
            data = {'output':out, 'type':"error"}
        with open("data_out/results/"+lang+"/" + file_name+'.txt','w') as f:
            f.write(result.stdout.decode("utf-8"))
        Del_Files(lang,file_name)
    except Exception as e:
        if subprocess.TimeoutExpired:
            data= {'output':"Code Timed out...", 'type':'error'}
        else:
            data = {'output':e, 'type':'error'}
    return data


def Del_Files(lang,file_name):
    try:
        file = b_dir+"/data_out/codes/"+lang+"/"+file_name+'.'+lang
        if os.path.isfile(file):
            os.remove(file)
        file = b_dir+"/data_out/results/"+lang+"/"+file_name+'.txt'
        if os.path.isfile(file):
            os.remove(file)
        if lang=='c':
            file_exe = b_dir+"/data_out/codes/c/"+file_name+'_exe.exe'
            if os.path.isfile(file_exe):
                os.remove(file_exe)
        elif lang=="cpp":
            file_exe = b_dir+"/data_out/codes/cpp/"+file_name+'_exe.exe'
            if os.path.isfile(file_exe):
                os.remove(file_exe)
    except OSError as e:
        pass