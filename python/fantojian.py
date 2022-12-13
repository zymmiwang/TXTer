
import sys
import zhconv
import fileinput

def fantojian(hant_str: str):
    return zhconv.convert(hant_str, 'zh-hans')


filename=sys.argv[1]
#filename="C:\\Users\\zym79\\Downloads\\test.txt"
#outname="C:\\Users\\zym79\\Downloads\\5.txt"
outname=sys.argv[2]

try:
    f = open(filename,'r')
    line = f.readline()               # 调用文件的 readline()方法，一次读取一行
    with open(outname,'a') as fe:
        while line:   
            fe.writelines(fantojian(line))                  
            line = f.readline()

            
except UnicodeDecodeError:
    f = open(filename,'r',encoding="utf-8")
    line = f.readline()               # 调用文件的 readline()方法，一次读取一行
    with open(outname,'a') as fe:
        while line:   
            fe.writelines(fantojian(line))                   
            line = f.readline()
    

with open(outname,'a') as fe:
    while line:   
        fe.writelines(fantojian(line))                 
        line = f.readline()

f.close()
fe.close()
print("ok")
