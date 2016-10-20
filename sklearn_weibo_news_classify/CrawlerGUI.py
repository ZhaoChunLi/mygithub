#coding=utf-8
import Tkinter
from Tkinter import*
from PIL import ImageTk
import tkFileDialog
from threading import *
import sys   
sys.setrecursionlimit(1000000) #例如这里设置为一百万  
import time
from getnewswithclass import url_thread

#import b from getnews
t=Tkinter.Tk()
t.title('System')
t.geometry('800x500')
t.resizable(width=False, height=False)
canvas = Canvas(t,width = 100, height=100, bg = 'white')
image = ImageTk.PhotoImage(file = r"F:\webcrawler1.jpg")
canvas.create_image(0, 0, image = image, anchor = NW)
canvas.create_text(400,50,text = '爬虫-分类系统 ',font=("宋体", 30),fill = 'black')
canvas.pack(fill=X,side=TOP,pady=10)
    
frr=Frame(t)
frr1=Frame(frr)
crawler_button=Tkinter.Button(frr1, text="去获取资料",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=2)
crawler_button.pack(pady=10)
classify_button1=Tkinter.Button(frr1, text="基于内容分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=2)
classify_button1.pack(pady=10)
classify_button2=Tkinter.Button(frr1, text="基于情感分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=2)
classify_button2.pack(pady=10)
frr1.pack()
frr.pack()
canvas2 = Canvas(t,width = 100, height=100, bg = 'white')
canvas2.create_image(0, 0, image = image, anchor = NW)
canvas2.create_text(400,50,text = '爬虫-分类系统 ',font=("宋体", 30),fill = 'black')
canvas2.pack(fill=X,side=BOTTOM)
def crawler():   
    top=Tkinter.Toplevel()
    top.title('CrawlerGUI')
    top.geometry('800x500')
    top.resizable(width=False, height=False)
    
    canvas4 = Canvas(top,width = 100, height=100, bg = 'gray')
    canvas4.create_line(10,10,800,10,fill="black", dash=(4, 4))
    canvas4.create_line(10,20,800,20,fill="black", dash=(4, 4))  
    canvas4.create_text(400,50,text = '爬虫-获取资料',font=("宋体", 30),fill = 'black')    
    canvas4.pack(fill=X,side=TOP)
    canvas4.create_line(10,80,800,80,fill="black",dash=(4, 4))
    canvas4.create_line(10,90,800,90,fill="black",dash=(4, 4))
    
    fr1=Frame(top)
    fr2=Frame(fr1)
    hit1=Tkinter. Label(fr2,text="基于内容分类的信息来源",font=("宋体", 15), width=25, height=2)
    hit1.pack(pady=10) 
    getnews_button=Tkinter.Button(fr2, text="获取新闻资料",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=2)
    getnews_button.pack(pady=10)
    Label(fr2,text="存储路径为：F:/新闻",font=("宋体", 12), width=50, height=2).pack(pady=10)
    kan2=Tkinter.Button(fr2,text="查看新闻爬取情况",bg='white',fg='black',font=("宋体", 12),command=None, width=25, height=2)
    kan2.pack(pady=10)
    fr2.pack(side=LEFT)
    
    fr3=Frame(fr1)
    hit2=Tkinter.Label(fr3,text="基于情感分类的信息来源",font=("宋体",15),width=25,height=2)
    hit2.pack(pady=10)
    getweibo_button=Tkinter.Button(fr3, text="获取微博资料",bg='white',fg='black',font=("宋体", 12),command=None, width=15, height=2)
    getweibo_button.pack(pady=10)
    Label(fr3,text="存储路径为：F:/微博",font=("宋体", 12), width=50, height=2).pack(pady=10)
    kan1=Tkinter.Button(fr3,text="查看微博爬取情况",bg='white',fg='black',font=("宋体", 12),command=None, width=25, height=2)
    kan1.pack()
    fr3.pack(side=RIGHT)   
    fr1.pack()
    fr5=Frame(top)
    hit3=Tkinter.Label(fr5,text="在分类前请先将数据进行合理选择和放置",font=("宋体",15),width=50,height=2)
    hit3.pack(side=BOTTOM)
    fr5.pack()
    class news_thread(Thread):
        from getnewswithclass import url_thread
        global get_news
        get_news=url_thread()
        def run(self):
            #self.doRecv=True
            if self.setDaemon==True:
               get_news.setDaemon=True
               get_news.start()
        def stop(self):
            print "wotingle"
            self.setDaemon=False
            get_news.stop()
           
               
    global news_th
    news_th=news_thread()
    global weiboThread
    weiboThread=None
    
    def news_start(): 
        news_th.setDaemon=True
        news_th.start() 
    #def news():
        #import getnewswithclass
    def weibo():
        from crawler import weibo_main
        
    def weibo_start():  
        import threading
        weiboThread =threading.Thread(target=weibo)
        weiboThread.setDaemon(True)
        weiboThread.start()   

    
    def look_weibo():
        filename = tkFileDialog.askopenfilename(initialdir = 'F:/微博')
    
    def look_news():
        filename = tkFileDialog.askopenfilename(initialdir = 'F:/新闻')
           
    getnews_button["command"]=news_start
    getweibo_button["command"]=weibo_start
    kan1["command"]=look_weibo
    kan2["command"]=look_news
def classifytool():
    top2=Tkinter.Toplevel()
    #top2.attributes("-alpha", 0.95)
    top2.title('ClassifyGUI')
    top2.geometry('800x700')
    top2.resizable(width=False, height=False)
    canvas4 = Canvas(top2,width = 100, height=100, bg = 'gray')
    canvas4.create_line(10,10,800,10,fill="black", dash=(4, 4))
    canvas4.create_line(10,20,800,20,fill="black", dash=(4, 4))  
    canvas4.create_text(400,50,text = '将获得的资料基于内容分类',font=("宋体", 30),fill = 'black')    
    canvas4.pack(fill=X,side=TOP)
    canvas4.create_line(10,80,800,80,fill="black",dash=(4, 4))
    canvas4.create_line(10,90,800,90,fill="black",dash=(4, 4))
    fr5=Frame(top2)   
    fr6=Frame(fr5)
    hint2=Tkinter. Label(fr6,text="请选择您要使用的分类器",font=("宋体", 15), width=25, height=2) 
    hint2.pack(pady=2)
    hint3=Tkinter. Label(fr6,text="KNN分类器",font=("宋体", 15), width=25, height=2) 
    hint3.pack(pady=2)
    feature_button=Tkinter.Button(fr6, text="特征值提取&生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=22, height=1)
    test_button=Tkinter.Button(fr6, text="生成测试集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    feature_button.pack(pady=5)
    test_button.pack(pady=5)
    KNN_button=Tkinter.Button(fr6, text="KNN分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    KNN_button.pack(pady=2)
    hint4=Tkinter. Label(fr6,text="Bayes分类器",font=("宋体", 15), width=25, height=2) 
    hint4.pack(pady=2)
    Bayes_button1=Tkinter.Button(fr6, text="生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    Bayes_button1.pack(pady=5)
    Bayes_button=Tkinter.Button(fr6, text="Bayes分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    Bayes_button.pack(pady=5)
    hint5=Tkinter. Label(fr6,text="普通分类器",font=("宋体", 15), width=25, height=2) 
    hint5.pack(pady=2)
    common_button1=Tkinter.Button(fr6, text="生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    common_button1.pack(pady=5)
    common_button=Tkinter.Button(fr6, text="普通分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    common_button.pack(pady=5)
    hint6=Tkinter. Label(fr6,text="sklearn实现",font=("宋体", 15), width=25, height=2) 
    hint6.pack(pady=2)
    sklearn_button=Tkinter.Button(fr6, text="sklearn集成分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    sklearn_button.pack(pady=5)
    fr6.pack(side=LEFT) 
      
    fr7=Frame(fr5)
    fr8=Frame(fr7)
    result_label=Tkinter.Label(fr8,text="结果显示",font=("宋体", 15),width=10,height=2)
    result_label.grid(row=1,column=1)
    result_KNN=Tkinter.Button(fr8, text="查看KNN分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_KNN.grid(row=0,column=2,pady=5)
    result_Bayes=Tkinter.Button(fr8, text="查看Bayes分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_Bayes.grid(row=1,column=2,pady=5)
    result_common=Tkinter.Button(fr8, text="查看普通分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_common.grid(row=2,column=2,pady=5)
    result_sklearn=Tkinter.Button(fr8, text="查看sklearn分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_sklearn.grid(row=3,column=2,pady=5)
    fr8.pack()
    fr9=Frame(fr7)   
    #result_text=Tkinter.Text(fr9,width=60,height=30,wrap='none')
    ys = Tkinter.Scrollbar(fr9, orient=Tkinter.VERTICAL)   
    xs= Tkinter.Scrollbar(fr9, orient=Tkinter.HORIZONTAL)     
    result_text = Tkinter.Text(fr9, width=60,height=30,yscrollcommand=ys.set,xscrollcommand=xs.set, wrap='none')
    xs.config(command=result_text.xview)  
    ys.config(command=result_text.yview)
    ys.pack(fill="y", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.N)  
    xs.pack(fill="x", expand=0, side=Tkinter.BOTTOM, anchor=Tkinter.N)  
    result_text.pack(fill="x", expand=1,pady=10)
    fr9.pack()
    fr7.pack(side=RIGHT,padx=40,pady=40)   
    fr5.pack()
    
    global KNNThread
    KNNThread=None
    def KNN_start():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器开始分类……')
        import threading
        KNNThread =threading.Thread(target=KNN)
        KNNThread.setDaemon(True)
        KNNThread.start()
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器分类完成。')
    def KNN():
        from classify_content import classify_content
    def result_show():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_content/result/result.txt'
        with open(path,'r') as f:                 
            lines=f.readlines() 
            for line in lines :
                result_text.insert(INSERT,line)
    def result_show3():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_content/bayes/result.txt'
        with open(path,'r') as f:                 
            lines=f.readlines() 
            for line in lines :
                result_text.insert(INSERT,line)
    def result_show4():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_content/common/result.txt'
        with open(path,'r') as f:                 
            lines=f.readlines() 
            for line in lines :
                result_text.insert(INSERT,line)
    def result_show5():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_content/result/result_sklearn.txt'
        with open(path,'r') as f:                 
            lines=f.readlines() 
            for line in lines :
                result_text.insert(INSERT,line)
    def get_feature():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器正在提取特征和生成训练集……')
        import Feature_content
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器提取了特征值并生成了训练集。')
    def test():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器正在生成测试集……')
        import Test_vectorize_content
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器测试集生成完成。')
    def Bayes_yuchuli():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器正在生成训练集……')
        import bayes_train_content
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器训练集生成完成。')
    def Bayes_start():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器正在分类……')
        import bayes_test_content
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器分类完成。')
    def common_yuchuli():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器正在生成训练集……')
        import common_train_content
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器训练集生成完成。')
    def common_start():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器正在分类……')
        import common_test_content 
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器分类完成。')  
    def sklearn_start():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'sklearn分类器正在分类……')
        import sklearn
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'sklearn分类器分类完成。')  
    KNN_button["command"]=KNN_start
    result_KNN["command"]=result_show
    result_Bayes["command"]=result_show3
    result_common["command"]=result_show4
    result_sklearn["command"]=result_show5
    feature_button["command"]=get_feature 
    test_button["command"]=test
    Bayes_button["command"]=Bayes_start
    Bayes_button1["command"]=Bayes_yuchuli
    common_button["command"]=common_start
    common_button1["command"]=common_yuchuli
    sklearn_button["command"]=sklearn_start
    
def classify_motion():
    top2=Tkinter.Toplevel()
    #top2.attributes("-alpha", 0.95)
    top2.title('ClassifyGUI')
    top2.geometry('800x700')
    top2.resizable(width=False, height=False)
    canvas4 = Canvas(top2,width = 100, height=100, bg = 'gray')
    canvas4.create_line(10,10,800,10,fill="black", dash=(4, 4))
    canvas4.create_line(10,20,800,20,fill="black", dash=(4, 4))  
    canvas4.create_text(400,50,text = '将获得的资料基于情感词分类',font=("宋体", 30),fill = 'black')    
    canvas4.pack(fill=X,side=TOP)
    canvas4.create_line(10,80,800,80,fill="black",dash=(4, 4))
    canvas4.create_line(10,90,800,90,fill="black",dash=(4, 4))
    fr5=Frame(top2)   
    fr6=Frame(fr5)
    hint2=Tkinter. Label(fr6,text="请选择您要使用的分类器",font=("宋体", 15), width=25, height=2) 
    hint2.pack(pady=2)
    hint3=Tkinter. Label(fr6,text="KNN分类器",font=("宋体", 15), width=25, height=2) 
    hint3.pack(pady=2)
    feature_button=Tkinter.Button(fr6, text="特征值提取&生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=22, height=1)
    #train_button=Tkinter.Button(fr6, text="生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    test_button=Tkinter.Button(fr6, text="生成测试集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    feature_button.pack(pady=5)
    #train_button.pack(pady=5)
    test_button.pack(pady=5)
    KNN_button=Tkinter.Button(fr6, text="KNN分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    KNN_button.pack(pady=2)
    hint4=Tkinter. Label(fr6,text="Bayes分类器",font=("宋体", 15), width=25, height=2) 
    hint4.pack(pady=2)
    Bayes_button1=Tkinter.Button(fr6, text="生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    Bayes_button1.pack(pady=5)
    Bayes_button=Tkinter.Button(fr6, text="Bayes分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    Bayes_button.pack(pady=5)
    hint5=Tkinter. Label(fr6,text="普通分类器",font=("宋体", 15), width=25, height=2) 
    hint5.pack(pady=2)
    common_button1=Tkinter.Button(fr6, text="生成训练集",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    common_button1.pack(pady=5)
    common_button=Tkinter.Button(fr6, text="普通分类",bg='white',fg='black',font=("宋体", 12),command=None,width=15, height=1)
    common_button.pack(pady=5)
    fr6.pack(side=LEFT) 
      
    fr7=Frame(fr5)
    fr8=Frame(fr7)
    result_label=Tkinter.Label(fr8,text="结果显示",font=("宋体", 15),width=10,height=2)
    result_label.grid(row=1,column=1)
    result_KNN=Tkinter.Button(fr8, text="查看KNN分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_KNN.grid(row=0,column=2,pady=5)
    result_Bayes=Tkinter.Button(fr8, text="查看Bayes分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_Bayes.grid(row=1,column=2,pady=5)
    result_common=Tkinter.Button(fr8, text="查看普通分类结果",bg='white',fg='black',font=("宋体", 12),command=None,width=20, height=1)
    result_common.grid(row=2,column=2,pady=5)
    fr8.pack()
    fr9=Frame(fr7)   
    #result_text=Tkinter.Text(fr9,width=60,height=30,wrap='none')
    ys = Tkinter.Scrollbar(fr9, orient=Tkinter.VERTICAL)   
    xs= Tkinter.Scrollbar(fr9, orient=Tkinter.HORIZONTAL)     
    result_text = Tkinter.Text(fr9, width=60,height=30, yscrollcommand=ys.set,xscrollcommand=xs.set, wrap='none')
    xs.config(command=result_text.xview)  
    ys.config(command=result_text.yview)
    ys.pack(fill="y", expand=0, side=Tkinter.RIGHT, anchor=Tkinter.N)  
    xs.pack(fill="x", expand=0, side=Tkinter.BOTTOM, anchor=Tkinter.N)  
    result_text.pack(fill="x", expand=1,pady=10)
    fr9.pack()
    fr7.pack(side=RIGHT,padx=40,pady=40)   
    fr5.pack()
    
    global KNNThread1
    KNNThread1=None
    def KNN_start1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器开始分类……')
        import threading
        KNNThread1 =threading.Thread(target=KNN1)
        KNNThread1.setDaemon(True)
        KNNThread1.start()
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器完成工作，请去查看结果。')
    def KNN1():
        from classify_motion import classify_motion
    def result_show1():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_motion/result/result.txt'
        with open(path,'r') as  f:       
            lines=f.readlines() 
            for line in lines:              
                result_text.insert(INSERT,line)
    def result_show2():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_motion/bayes/result.txt'
        with open(path,'r') as  f:       
            lines=f.readlines() 
            for line in lines:              
                result_text.insert(INSERT,line)
    def result_show_common():
        result_text.delete(0.0, END)
        path=r'F:/classify/classify_motion/common/result.txt'
        with open(path,'r') as  f:       
            lines=f.readlines() 
            for line in lines:              
                result_text.insert(INSERT,line)
    def get_feature1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器正在提取特征和生成训练集……')
        import Feature_motion
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器提取了特征值并生成了训练集。')
    def test1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器正在生成测试集……')
        import Test_vectorize_motion
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'KNN分类器测试集生成完成。')
    def Bayes_yuchuli1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器正在生成训练集……')
        import bayes_train_motion
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器训练集生成完成。')
    def Bayes_start1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器正在分类……')
        import bayes_test_motion
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'Bayes分类器分类完成。')
    def common_yuchuli1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器正在生成训练集……')
        import common_train_motion
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器训练集生成完成。')
    def common_start1():
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器正在分类……')
        import common_test_motion 
        result_text.delete(0.0, END)
        result_text.insert(INSERT,'普通分类器分类完成。')  
    KNN_button["command"]=KNN_start1
    result_KNN["command"]=result_show1
    result_Bayes["command"]=result_show2
    result_common["command"]=result_show_common
    feature_button["command"]=get_feature1 
    #train_button["command"]=train1
    test_button["command"]=test1
    Bayes_button["command"]=Bayes_start1
    Bayes_button1["command"]=Bayes_yuchuli1
    common_button["command"]=common_start1
    common_button1["command"]=common_yuchuli1

#if __name__=='__main__':   
crawler_button["command"]=crawler    
classify_button1["command"]=classifytool
classify_button2["command"]=classify_motion
Tkinter.mainloop()

