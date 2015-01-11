__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import time
from datetime import datetime



def video_viewcnt(video_url, p_id): 
    try:
        html = urlopen(video_url).read()
        soup = BeautifulSoup(html) 
    except ValueError:
        return (-2, "facebook", "invalid", datetime.now())
    
    if video_url.startswith("https://www.facebook.com/video.php") == True:
        items = soup.find("div", {"class" : "fbPhotosMediaInfo"}).findAll("span", {"class" : "fcg"})
        try:
            c = items[2].get_text(strip=True).replace(",", "")
        except IndexError:
            return None         #if it's external video link, there's no viewcount
        
        regex_str = "([0-9]+)"
        c = re.search(regex_str, c)
        cnt = c.group(0)
        v_source = "facebook"
        
    elif video_url.startswith("http://youtu.be") or video_url.startswith("http://www.youtube.com") == True:
        try:
            cnt = soup.find(id = "watch-view-count").get_text(strip=True).replace(",", "")
        except AttributeError:
            cnt = -1
        cnt = int(cnt)
        v_source = "youtube"
        
    elif video_url.startswith("http://news.sbs.co.kr") == True:
        if "jsp" in video_url:
            real_url = soup.findAll("meta")[2]['content']
            real_url = real_url.split(";url=")[1]       #redirected
            return video_viewcnt(real_url, p_id)
        
        else:
            cnt = soup.find("em", {"class": "sed_atc_num"}).get_text(strip=True).replace(",", "")
            cnt = int(cnt)
            v_source = "sbs news"
        
    else:
        print(video_url)
        
    return (cnt, v_source, video_url, datetime.now())
    




if __name__ == "__main__":
    url = "https://www.facebook.com/video.php?v=1013252018690315"
    #https://www.facebook.com/video.php?v=782070041808515        #there's no viewcnt
    p_id=100
    (view_cnt, v_source, retrieved_time) = video_viewcnt(url,p_id)
    
    print(view_cnt)
    print(v_source)
    print(retrieved_time)