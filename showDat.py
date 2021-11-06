import matplotlib.pyplot as plt
    
def autolabel(rects):
 for rect in rects:
  height = rect.get_height()
  plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height))
    
def showDat():
    x1=[]
    x2=[]
    y1=[]
    y2=[]
    totalCounter=0
    #读取实验数据
    with open('res.dat','r',encoding='utf-8')as file:
        res=file.readline()
        
        while not res=='':
            res=eval(res)
            totalCounter=res['total']
            #统计目标数字设置与胜率的关系
            x1.append(res['target'])
            x2.append(res['target'])
            y1.append(res['x1']/totalCounter)
            y2.append(res['x2']/totalCounter)
            res=file.readline()
    plt.ylabel('winning rate')
    plt.xlabel('t0')
    
    plt.plot(x2,y2)
    plt.plot(x1,y1)
    
    plt.legend(['firsthand','backhand'])
    plt.title('Correlation between t0 and winning rate')
    
    plt.show()
    #统计并比较两人总体胜率
    a=plt.bar(['firsthand','backhand'],[int(sum(y2)*totalCounter),int(sum(y1)*totalCounter)])
    autolabel(a)
    
    plt.title('Number of victories in a billion games')
    plt.ylabel('winning count')
    
    plt.show()
    print(sum(y1)/totalCounter)
    print(sum(y2)/totalCounter)

    
if __name__=="__main__":

	showDat()

