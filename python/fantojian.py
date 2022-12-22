
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
            try:
                a=fantojian(line)                
                fe.writelines(fantojian(a))                  
                line = f.readline()  
            except:#过滤特殊字符
                for i in range(0,len(line)-1):
                    try:
                        line[i]=fantojian(str(line[i]))
                    except:
                        line[i]=line[i]
                        
                fe.writelines(line)                  
                line = f.readline()  
                 


 #utf-8           
except UnicodeDecodeError:
    f = open(filename,'r',encoding="utf-8")
    line = f.readline()               # 调用文件的 readline()方法，一次读取一行
    with open(outname,'a',encoding="utf-8") as fe:
        while line:
            try:
                a=fantojian(line)                
                fe.writelines(fantojian(a))                  
                line = f.readline()  
            except:#过滤特殊字符
                for i in range(0,len(line)-1):
                    try:
                        line[i]=fantojian(str(line[i]))
                    except:
                        line[i]=line[i]
                fe.writelines(line)                  
                line = f.readline()  

            
    

with open(outname,'a') as fe:
    while line:   
        fe.writelines(fantojian(line))                 
        line = f.readline()

f.close()
fe.close()
print("ok")
