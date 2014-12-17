from bs4 import BeautifulSoup as bs
import requests
import re
from datetime import date, timedelta, datetime
import time
import random
import os


s = requests.Session()
my_referer = "http://cafeblog.search.naver.com/search.naver?where=post&query=%EB%B6%80%EC%82%B0&ie=utf8&st=date&sm=tab_opt&date_from=20130101&date_to=20130102&date_option=6&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Afrom20130101to20130102&mson=0"
user_agent = {'User-agent': 'Mozilla/5.0'}
s.headers.update({'referer': my_referer})
s.headers.update({'user_agent':user_agent})

