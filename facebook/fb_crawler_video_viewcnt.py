__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import time

from fb_video import video_viewcnt
from easy_db import easy_mysql, insert_mysql



if __name__ == "__main__":
    
    os.environ['TZ'] = ':Asia/Seoul'; time.tzset()       #time zone setting
    
    cfg_dict = dict(host='sbsnews.crsrypkw7bkm.ap-northeast-1.rds.amazonaws.com', usr='root', pwd='hqam30018', 
                    db='FACEBOOK')
    
    (con, cur) = easy_mysql(cfg_dict)
    cur.execute("SET NAMES latin1")         # couldn't changed RDS's character_set_server....
    
    cur.execute("SELECT p_id, p_link FROM post WHERE p_type = 'video';")
    urls = cur.fetchall()
    print("fetching all video urls finished...")
    print("the number of videos: %i" % len(urls))
    
    n = 0
    for row in urls:
        n += 1
        p_id = row[0]
        v_url = row[1]
        
        try:
            (view_cnt, v_source, real_url, when) = video_viewcnt(v_url, p_id)
            
        except TypeError:
            cur.execute("SELECT p_message FROM post WHERE p_id = %i" % p_id)
            for m in cur:
                indx = m[0].find("http://news.sbs.co.kr")
                v_url = m[0][indx:]
                print(v_url)
                (view_cnt, v_source, real_url, when) = video_viewcnt(v_url, p_id)
                if real_url == "invalid":
                    real_url = row[1]
        var_tuple = (p_id, view_cnt, v_source, real_url, when)
        
        try:
            sql = "INSERT INTO video(p_id, view_cnt, v_source, v_url, last_update) VALUES(%i, %i, '%s', '%s', '%s');"
            insert_mysql(cur, sql, var_tuple)
        except TypeError:
            print(var_tuple)
        con.commit()
        
        if n%500 == 0:
            print("%i finished" % n)

    print("all finished")
    
    
    