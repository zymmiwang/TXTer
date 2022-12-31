import sys

num=int(sys.argv[1])
outname=sys.argv[num+2]
fe=open(outname,'a',encoding="utf-8")
for i in range(0,num):
    filename=sys.argv[i+2]
    
    try:
        f = open(filename,'r')
        line = f.readline()               # 调用文件的 readline()方法，一次读取一行
        
        while line:               
            fe.writelines(line)                  
            line = f.readline()
        fe.writelines("\n") 
                
                 
         #utf-8           
    except UnicodeDecodeError:
        f = open(filename,'r',encoding="utf-8")
        line = f.readline()               # 调用文件的 readline()方法，一次读取一行
            
        while line:              
            fe.writelines(line)                  
            line = f.readline()
        fe.writelines("\n") 
        
    f.close()


    
fe.close()
print("ok")
