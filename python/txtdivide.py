import sys

filename=sys.argv[1]
outfile=sys.argv[2]
num=int(sys.argv[3])
#fe=open(outname,'a',encoding="utf-8")
count=0
n=1
s=0
try:
    f = open(filename,'r')
    line = f.readline()               # 调用文件的 readline()方法，一次读取一行
        
    while line:
        count+=1                
        line = f.readline()
            
    f.close()
    f = open(filename,'r')
    line1 = f.readline()
    while line1:
        s+=1

        if s==1 and n==1:
            fe=open(outfile+"\\1.txt",'a')

        outname=outfile+"\\"+str(n)+".txt"
        fe=open(outname,'a')
        fe.writelines(line1)                  
        line1 = f.readline()
        
        if s>=count//num and n<=num-1:
            s=0
            n+=1
            fe.close()
        
        
    fe.close()
                
                 
         #utf-8           
except UnicodeDecodeError:
    f = open(filename,'r',encoding="utf-8")
    line = f.readline()               # 调用文件的 readline()方法，一次读取一行
            
    while line:
        count+=1
        line = f.readline()


    f.close()
    f = open(filename,'r',encoding="utf-8")
    line1 = f.readline()
    while line1:
        s+=1
        if s==1 and n==1:
            fe=open(outfile+"\\1.txt",'a')

        outname=outfile+"\\"+str(n)+".txt"
        fe=open(outname,'a',encoding="utf-8")    
        fe.writelines(line1)                  
        line1 = f.readline()
        
        if s>=count//num and n<=num-1:
            s=0
            n+=1
            fe.close()
            
        
    fe.close()
        
f.close()
print("ok")
