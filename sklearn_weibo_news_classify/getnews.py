
#coding=utf-8
import os
import codecs
from lxml import etree
from time import sleep
import urllib2
import re
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')

def addurl(url,visitedurl,unvisitedurl):
    if url and (url in visitedurl) and (url not in unvisitedurl):
        unvisitedurl.append(url)
    return True
    
def save_content(url,path):   
    html = urllib2.urlopen(url).read().decode('gbk')
    html=re.sub('<div class="otitle">.*?</div>','',html)
    #print html
    pattern = re.compile('<div id="p_content".*?>(.*?)</div>',re.S)
    result = re.search(pattern,html)
    #print result.group(1)
    if result:
        patternp1 = re.compile('<p.*?>(.*?)</p>',re.S)
        patternp2 = re.compile('<P.*?>(.*?)</P>',re.S)
        resultp1 = re.findall(patternp1,result.group(1))
        resultp2 = re.findall(patternp2,result.group(1))
        if resultp1:
            with open(path,'a+') as f:
                for parag in resultp1:
                    #print parag
                    parag_content=re.sub('<script.*?>.*?</script>','',parag)
                    parag_content=re.sub('&nbsp','',parag_content)
                    parag_content =re.sub('<.*?>','',parag_content)
                    f.write(parag_content)
                    
        if resultp2:
             with open(path,'a+') as f:
                for parag in resultp2:
                    #print parag
                    parag_content=re.sub('<script.*?>.*?</script>','',parag)
                    parag_content=re.sub('&nbsp','',parag_content)
                    parag_content =re.sub('<.*?>','',parag_content)
                    f.write(parag_content)
    else:
        catch_content(url,path,html)
 
def  catch_content(url,path,html):
    pattern1= re.compile('<div class="m_text".*?>(.*?)</div>',re.S)
    result1= re.search(pattern1,html)
    if result1:
        patternp1 = re.compile('<p.*?>(.*?)</p>',re.S)
        resultp1 = re.findall(patternp1,result1.group(1))
        with open(path,'a+') as f:
            for parag in resultp1:
                #print parag
                parag_content=re.sub('<script.*?>.*?</script>','',parag)
                parag_content=re.sub('&nbsp','',parag_content)
                parag_content =re.sub('<.*?>','',parag_content)
                f.write(parag_content)
    else:
        pattern2= re.compile('<p style="text-indent: 2em;".*?>(.*?)</p>',re.S)
        result2= re.findall(pattern2,html)
        if result2:
            with open(path,'a+') as f:
                for p in result2:
                    parag_content=re.sub('<script.*?>.*?</script>','',p)
                    parag_content=re.sub('&nbsp','',parag_content)
                    parag_content =re.sub('<.*?>','',parag_content)
                    f.write(parag_content)
        else:
            pattern3= re.compile('<div class="text_show".*?>(.*?)</div>',re.S)
            result3= re.search(pattern3,html)
            if result3:
                patternp4 = re.compile('<p.*?>(.*?)</p>',re.S)
                resultp4 = re.findall(patternp4,result3.group(1))
                with open(path,'a+') as f:
                    for p in resultp4:
                        parag_content=re.sub('<script.*?>.*?</script>','',p)
                        parag_content=re.sub('&nbsp','',parag_content)
                        parag_content =re.sub('<.*?>','',parag_content)
                        f.write(parag_content)
            
          
def geturls_thetitle(url,visitedurl):
    path=''
    try:
        html = urllib2.urlopen(url,timeout=8).read().decode('gbk')
        title_tree=etree.HTML(html)
        ptitle=re.compile('<title>(.*?)</title>')
        rtitle=re.search(ptitle,html)
        if rtitle:
            title=rtitle.group(1)
            puretitle=beautiful(title)
            #新加入的内容开始
            print title
            news_class=getclass(url)
            #path_of_class=(r'f:/新闻2/'+news_class).decode('utf-8')
            #if not os.path.isdir(path_of_class):
                #os.makedirs(path_of_class)
            #path=(path_of_class+'/'+path_of_class+'_'+puretitle+'.txt').decode('utf-8')
            path=(r'f:/新闻10/'+news_class+'_'+puretitle+'.txt').decode('utf-8')
            if os.path.exists(path):
                return False
            pattern = re.compile('<div class="zdfy clearfix">(.*?)</div>',re.S)
            result = re.search(pattern,html)
            if not result:
        #没有div标签
                print "单页1"        
                save_content(url,path)
            elif result.group(0):
                r=re.sub('<.*?>','',result.group(0))
                if r:
                    print "多页"
                    pattern1=re.compile('(<a.*?>)',re.S)
                    nexturls=re.findall(pattern1,result.group(1))
                    linkp=re.compile('(.*?)/n/.*?',re.S)
                    halflink=re.search(linkp,url).group(1)
                    for nexturl in nexturls:
                        a=re.compile(r'href="(.*?)"',re.S)
                        n=re.search(a,nexturl).group(1)
                        newnexturl=halflink+n
                        print newnexturl
                        save_content(newnexturl,path) 
                else:
            #有div标签，但是标签内容为空
                    print "单页2"
                    save_content(url,path)
            else:
                print "不符合格式的网页，跳过"
                return False
        visitedurl.append(url)
    #此处删除空文件,因为存在标签被斩断的问题，所以会有空文件存在，解决的话是很费劲儿的，而且是太多样的
        kongma=os.path.getsize(path)
        if kongma==0:
            os.remove(path)
    except Exception,e:
        return False
        
    
def get_homepage(url,visitedurl,unvisitedurl):
    html = urllib2.urlopen(url).read().decode('gbk')
    pattern_link=re.compile('<a href="(.*?)".*?>.*?</a>',re.S)
    links=re.findall(pattern_link,html)
    for link in links:
        if "people.com.cn/" in link and "/n1/"in link and "www" not in link:
        #if "people.com.cn/" in link and "www" not in link:
            print link
            addurl(link,visitedurl,unvisitedurl)
            geturls_thetitle(link,visitedurl)
        else:
            continue
    begin=0
    end=len(unvisitedurl)
    go_on(visitedurl,unvisitedurl,begin,end)
   
    
def beautiful(s):
    ss=s.replace('*','').replace('\\','').replace('/','').replace(':','').replace('?','').replace('"','')
    ss=ss.replace('<','').replace('>','').replace('|','').replace('&nbsp;','')
    ss=ss.strip()
    return ss

def getclass(url):
    spliturl=url.split('.')
    beforeurl=spliturl[0]
    class_of_news=beforeurl.replace('http://','').strip()
    return class_of_news
    

def go_on(visitedurl,unvisitedurl,begin,end):
    print "恭喜，成功到达下一页"
    for url in unvisitedurl[begin:end]:        
        html = urllib2.urlopen(url).read().decode('gbk')
        pattern_link=re.compile('<a href="(.*?)".*?>.*?</a>',re.S)
        links=re.findall(pattern_link,html)
        for link in links:
            if "people.com.cn/" in link and "/n1/"in link and "www" not in link:
                print link
                addurl(link,visitedurl,unvisitedurl)
                geturls_thetitle(link,visitedurl)
            else:
                continue
    newend=len(unvisitedurl)
    go_on(visitedurl,unvisitedurl,end,newend) 
    
visitedurl=[]
unvisitedurl=[]
url='http://www.people.com.cn/'
get_homepage(url,visitedurl,unvisitedurl)
