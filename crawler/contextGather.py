from moduleControl import *

def blogContextGather(blogInfo):
    global counnn
    blog_url = blogInfo[0]
    blog_short =  blogInfo[1]
    blog_date = blogInfo[2] 
    
    aaa= open('pusan'+'.txt','a',encoding='utf8')
    try:
        if 'naver.com' in blog_url:
            blog_text =  naver_blog(blog_url)
        elif 'daum.net' in blog_url:
            blog_text = daum_blog(blog_url)
        elif 'egloos.com' in blog_url:
            blog_text = egloos_blog(blog_url)
        elif 'tistory.com' in blog_url:
            blog_text = tistory_blog(blog_url)
        else:
            blog_text = ''
        if blog_text == '':
            return dict({'blog_url' : blog_url, 'blog_short' : blog_short ,'blog_date' : blog_date, 'blog_text' : '')
        else:
            return dict({'blog_url' : blog_url, 'blog_short' : blog_short ,'blog_date' : blog_date, 'blog_text' : blog_text)
    except Exception as e:
        return dict({'blog_url' : blog_url, 'blog_short' : blog_short ,'blog_date' : blog_date, 'blog_text' : '')
        #print(e,blog_url)



def naver_blog(url):
    blog_data = bs(requests.get('http://m.'+url).text)
    blog_text = blog_data.find('div','post_ct').text
    return blog_text

def daum_blog(url):
    blog_data = bs(requests.get('http://m.'+url).text)
    blog_text = blog_data.select('div[id=article]')[0].text
    return blog_text

def tistory_blog(url):
    blog_data = bs(requests.get('http://'+url).text)
    blog_text = blog_data.select('div[class=article]')[0].text
    return blog_text

def egloos_blog(url):
    blog_data = bs(requests.get('http://'+url).text)
    blog_text = blog_data.select('div[class=hentry]')[0].text
    return blog_text

def anomous_blog(url,blog_short):
    blog_data = bs(requests.get('http://'+url).text)
    len_test = blog_data.select('frame')[0]['src']
    if len(len_test)>0:
        tmp = bs(requests.get(len_test).text)
        tmp_url = len_test.split('/')[2]+(tmp.select('frame')[0]['src'])
        if 'naver' in tmp_url:
            return naver_blog(tmp_url)
        if 'daum' in tmp_url :
            return daum_blog
        else:
            return ''
    else:
        return ''
