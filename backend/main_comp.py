import uuid
import subprocess
import os


def main_comp_all(codedata,lang,input_text):
    try:
        file_name = str(uuid.uuid4())
        with open("codes/"+lang+"/" + file_name+'.'+lang,'w') as f:
            f.write(codedata)
        if lang=="py":
            if input_text:
                result = subprocess.run(["D:/Django/nvscompiler/Scripts/python.exe","codes/py/"+file_name+'.'+lang], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                result = subprocess.run(["D:/Django/nvscompiler/Scripts/python.exe","codes/py/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="js":
            result = subprocess.run(["node","codes/js/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="cpp":
            result = subprocess.run(["g++","codes/cpp/"+file_name+'.'+lang,"-o","codes/cpp/"+file_name+"_exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                result = subprocess.run(["codes/cpp/"+file_name+"_exe"], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="c":
            result = subprocess.run(["gcc","codes/c/"+file_name+'.'+lang,"-o","codes/c/"+file_name+"_exe"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode == 0:
                result = subprocess.run(["codes/c/"+file_name+"_exe"], input=input_text.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if lang=="php":
            result = subprocess.run(["C:/xampp/php/windowsXamppPhp/php.exe","codes/php/"+file_name+'.'+lang], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            data = {'output':result.stdout.decode("utf-8"),'type':"success"}
        else:
            out = result.stderr.decode("utf-8")
            out = out.replace("codes/"+lang+"/"+file_name+'.'+lang,"main."+lang)
            out = out.replace("D:\\django_projects\\venv-compiler\\nvscompiler\\codes\\"+lang+"\\"+file_name+'.'+lang,"main."+lang)
            data = {'output':out, 'type':"error"}
        with open("results/"+lang+"/" + file_name+'.txt','w') as f:
            f.write(result.stdout.decode("utf-8"))
        try:
            file = "D:/django_projects/venv-compiler/nvscompiler/codes/"+lang+"/"+file_name+'.'+lang
            if os.path.isfile(file):
                os.remove(file)
            file = "D:/django_projects/venv-compiler/nvscompiler/results/"+lang+"/"+file_name+'.txt'
            if os.path.isfile(file):
                os.remove(file)
            if lang=='c':
                file_exe = "D:/django_projects/venv-compiler/nvscompiler/codes/c/"+file_name+'_exe.exe'
                if os.path.isfile(file_exe):
                    os.remove(file_exe)
            elif lang=="cpp":
                file_exe = "D:/django_projects/venv-compiler/nvscompiler/codes/cpp/"+file_name+'_exe.exe'
                if os.path.isfile(file_exe):
                    os.remove(file_exe)
        except OSError as e:
            pass
    except Exception as e:
        data = {'output':e, 'type':'error'}
    return data