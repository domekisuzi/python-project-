# from pyecharts.charts import Bar
# from pyecharts import options as opts
import re

file = "C:\\Users\\domek\\Documents\\Tencent Files\\1076839874\\FileRecv\\1.txt"
f = open(file,encoding="utf-8")
data = f.readlines()
f.close()
a = 0
b = 0
c = 0
d = 0
default=0
print(data)
dct = {
}
ab=0
ac=0
ad=0
bc=0
bd=0
cd=0
abc=0
abd=0
acd=0
bcd=0
abcd=0
l = []
for i in data:
    # if re.match("（D）", i):
    #     d += 1
    # elif re.match("（C）", i):
    #     c += 1
    # elif re.match("（B）", i):
    #     b += 1
    # elif re.match("（A）", i):
    #     a += 1
    # elif re.match('我',i):
    #     default+=1
    if i.endswith("（D）\n"):
        d += 1
    elif i.endswith("（C）\n"):
        c += 1
    elif i.endswith("（B）\n"):
        b += 1
    elif i.endswith("（A）\n"):
        a += 1
    elif i.endswith("（AB）\n"):
        ab+=1
    elif i.endswith("（AC）\n"):
        ac+=1
    elif i.endswith("（AD）\n"):
        ad+=1

    elif i.endswith("（BD）\n"):
        bd+=1
    elif i.endswith("（BC）\n"):
        bc+=1
    elif i.endswith("（CD）\n"):
        cd+=1
    elif i.endswith("（ABC）\n"):
        abc += 1
    elif i.endswith("（ABD）\n"):
        abd += 1
    elif i.endswith("（ACD）\n"):
        acd += 1
    elif i.endswith("（BCD）\n"):
        bcd += 1
    elif i.endswith("（ABCD）\n"):
        abcd += 1
    l.append(re.findall('（[ABCDE]{2,5}）',i))



print(l)
print("a",a,"b",b,"c",c,"d",d)
print("ab:",ab,"ac:",ac,"ad:",ad,"bc:",bc,"bd:",bd,"cd:",cd,"abc:",abc,"abd",abd,"acd:",acd,"bcd:",bcd,"abcd",abcd)