import urllib.request as request  
import urllib.parse as parse  
import string  
print(""" 
+++++++++++++++++++++++ 
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    for i in range(begin_page, end_page + 1):  
        sName = 'f:/test/'+str(i).zfill(2)+'.html'  #自动填充为6位的文件名
        print('下载第'+str(i)+'个页面, 保存为'+sName)  
        m = request.urlopen(url+str(i)).read()  
        with open(sName,'wb') as file:  
            file.write(m)  
        file.close()  
if __name__ == "__main__":  
    url = "http://tieba.baidu.com/p/"  
    begin_page = 1  
    end_page = 5  
    baidu_tieba(url, begin_page, end_page)  
