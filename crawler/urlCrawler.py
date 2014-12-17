from moduleControl import *

from keywordlist import keywordList

def make_date(input_date):
        string_date=''
        for s in input_date.isoformat().split('-'):
            string_date+=str(s)
        return string_date


def blogUrl(keyword,startDate,endDate,urlStack):
    global s
    my_referer = "http://cafeblog.search.naver.com/search.naver?where=post&query=%EB%B6%80%EC%82%B0&ie=utf8&st=date&sm=tab_opt&date_from=20130101&date_to=20130102&date_option=6&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Afrom20130101to20130102&mson=0"
    s.headers.update({'referer': my_referer})
    initial_date_fm=date(int(startDate.split(',')[0]),int(startDate.split(',')[1]),int(startDate.split(',')[2]))
    final_date_fm =date(int(endDate.split(',')[0]),int(endDate.split(',')[1]),int(endDate.split(',')[2]))
    start_date_fm = initial_date_fm
    for query in keywordList(keyword):
        while(start_date_fm != final_date_fm):
            next_date_fm = start_date_fm + timedelta(1)
            start_date=make_date(start_date_fm)
            end_date=make_date(next_date_fm)
            url="http://cafeblog.search.naver.com/search.naver?where=post&query="+query+"&ie=utf8&st=date&sm=tab_opt&date_from="+start_date+"&date_to="+end_date+"&date_option=6&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Afrom"+start_date+"to"+end_date+"&mson=0"
            page_source = requests.get(url, headers=user_agent).text
            page_count=int(bs(page_source).find('span','title_num').text.split('/')[1].replace(' ','')[:-1].replace(',',''))//10
            for a in range(1,page_count+1):
                page_url =url+"&start="+ str((a-1)*10+1)
                list_source = requests.get(page_url,headers=user_agent).text
                tmp = bs(list_source)
                tmp_list = tmp.find_all('dl')
                for blog_tmp in tmp_list:
                    try:
                        blog_date = blog_tmp.find('dd','txt_inline').text.split(' ')[0]
                    except :
                        continue
                    if blog_date.find('시간')>-1:
                        blog_date=start_date
                    if blog_date.find('일전')>-1:
                        blog_date = make_Date(start_date_fm-timedelta(int(blog_date.split('일전')[0])))

                    blog_url=blog_tmp.find('span','inline').text.split(' ')[1]
                    blog_short = blog_tmp.find('dd','sh_blog_passage').text.split('...')
                    #print(blog_url)
                    urlStack.put([blog_url,blog_short,blog_date,query])
            start_date_fm=next_date_fm
