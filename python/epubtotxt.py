from epub2txt import epub2txt
import sys

#filepath = "C:\\Users\\zym79\\Downloads\\镰池和马 - 新約魔法禁書目錄22.epub"
filepath=sys.argv[1]
#outpath = "C:\\Users\\zym79\\Downloads\\镰池和马 - 新約魔法禁書目錄22.txt"
outpath=sys.argv[2]

res = epub2txt(filepath)

try:
    with open(outpath,'a',encoding="utf-8") as f:
        f.writelines(res)
        
except UnicodeDecodeError:
    with open(outpath,'a',encoding="utf-8") as f:
        f.writelines(res)
        
print("ok")

