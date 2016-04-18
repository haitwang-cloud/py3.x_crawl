import urllib  
import urllib.request as request  
from bs4 import BeautifulSoup  
def taobao(url):  
    response = request.urlopen(url)  
    html = response.read()  
    #win7系统，默认是gdk要先解码，再用utf8编码就可以显示汉字了  
    data = html.decode('gbk').encode('utf-8')  
    soup = BeautifulSoup(data)  
    for list in soup.find_all('h3'):  
        print(list.string)  
if __name__ == '__main__':  

    url = 'http://www.taobao.com/?spm=a310q.2219005.1581860521.1.b9kUd4'  
    taobao(url)  
