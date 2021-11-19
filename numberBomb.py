import random
import matplotlib.pyplot as plt
import os
import showData



counter=0

def guessNum(start,end,t):
    global counter
    counter+=1

    r=random.randint(start,end)
    #根据猜测的数字调整范围
    if r==t:
        return
    elif r<t:
        start=r+1
    else:
        end=r-1
    #print(r)
    #递归，直至猜中
    guessNum(start,end,t)

def init():
    #程序产生的数据是追加输入，所以要先删除上次运行程序留下的数据。这里是Linux下的命令。如果是windows系统，酌情修改
    os.system("rm -f data.csv")
    os.system("rm -f res.dat")

def dealData(counters,target):
    #判断甲乙两人的胜负情况，进行的局数，并封装为字典
    x1=x2=0  #x1 x2分别代表甲和乙的胜负局数
    for i in counters:
        if i%2:
            x2+=1
        else:
            x1+=1
    res={'target':target,'total':len(counters),'x1':x1,'x2':x2}
    return res


def main():
    init()
    global counter
    n=100
    counters=[]
    results=[]
    
    #遍历t0的取值，每个取值下进行重复次实验
    for i in range(1,101):
        print("target number:{}".format(i))
        #重复实验的次数
        for j in range(n):
            guessNum(1,100,i)
            #print(counter)
            counters.append(counter)
            counter=0
        with open('data.csv','w+',encoding='utf-8')as file:
            file.write(str(counters))

        #统计实验数据
        res=dealData(counters,i)
        results.append(res)
        #print(counters)
        counters=[]
    with open('res.dat','w',encoding='utf-8')as file:
        for i in results:
            file.write(str(i)+'\n')

    showData.showDat()


if __name__ == '__main__':
    main()

