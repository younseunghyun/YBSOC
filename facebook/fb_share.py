__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.
"""

from datetime import datetime
import time
import os
import types

from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


#sudo apt-get install firefox
#sudo apt-get install xvfb




def replace_with_newlines(element):
    text = ''
    for elem in element.recursiveChildGenerator():
        if isinstance(elem, str):
            text += elem.strip()
        elif elem.name == 'br':
            text += '\n'
    return text




def parse_html(html, p_id): 
    return_list = list()
    soup = BeautifulSoup(html)
    shares = soup.find(id = "view_shares_dialog_%i" % p_id).findAll("div", {"class": "_4-u2 mbm _5jmm _5pat _5v3q"})
    
    for share in shares:
        try:
            s_datetime = share.find("abbr", {"class": "_5ptz timestamp livetimestamp"})['data-utime']
        except TypeError:
            s_datetime = share.find("abbr", {"class": "_5ptz"})['data-utime']
        s_datetime = datetime.fromtimestamp(int(s_datetime))
            
        s_messages = share.find("div", {"class": "_5pbx userContent"})
        s_message = ""
        if s_messages != None:
            s_messages = s_messages.findAll("p")
            for s in s_messages:
                s_message += "\n" + replace_with_newlines(s)
        s_message = s_message.replace("\'", "\\'")
        
        profile = share.find("div", {"class": "fwn fcg"}).findAll("a")  
        usr_info = profile[0]['data-hovercard'].split(".php?")
        usr_name = profile[0].get_text(strip=True).replace("\'", "\\'")
        usr_type = usr_info[0].split("/")[3]
        
        if "directed_target_id" in usr_info[1]:     #share to the other location such as group
            try:
                target_info = profile[1]['data-hovercard'].split(".php?")
                target_name = profile[1].get_text(strip=True).replace("\'", "\\'")
            except KeyError:
                target_info = profile[2]['data-hovercard'].split(".php?")
                target_name = profile[2].get_text(strip=True).replace("\'", "\\'")
            usr_id = int(usr_info[1].split("&")[0][3:])
            target_type = target_info[0].split("/")[3]
            target_id = int(target_info[1].split("&")[0][3:])
            return_list.append((p_id, usr_id, usr_name, usr_type, s_datetime, s_message[1:], target_id, target_name, target_type))
        elif "extragetparams" in usr_info[1]:
            usr_id = int(usr_info[1].split("&")[0][3:])
            return_list.append((p_id, usr_id, usr_name, usr_type, s_datetime, s_message[1:]))
        else:
            usr_id = int(usr_info[1][3:])
            return_list.append((p_id, usr_id, usr_name, usr_type, s_datetime, s_message[1:]))
        
    return return_list





def save_share_html(file_path, file_name):
    file_path = "/home/ubuntu/py/facebook/150110_share/"
    file_name = str(p_datetime)[:10] + "_" + str(p_id) + ".html"
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    open(file_path + file_name,'w').write(share_html)





def get_fb_share(browser, p_id):
    share_url = "https://www.facebook.com/shares/view?id=%i" % p_id
    browser.get(share_url)
    when = datetime.now()
    elem = browser.find_element_by_tag_name("body")
    try:
        elem.find_element_by_css_selector("#view_shares_dialog_%i" % p_id)
    except NoSuchElementException:
        return ("no shares", when)      #if there's no share at all, stop here

    no_of_pagedowns = 5
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.8)
        no_of_pagedowns -= 1
    time.sleep(1)

    while True:
        try:
            elem.find_element_by_css_selector('.clearfix.uiMorePager.stat_elem')
            print("there's more shares... loading...")
            no_of_pagedowns = 5
            while no_of_pagedowns:
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.8)
                no_of_pagedowns -= 1
            time.sleep(1)
        except NoSuchElementException:        #if there's no more shares, return values
            print("there's no more shares... stop loading and return...")
            return (browser.page_source, when)





def fb_login(browser, email, pwd):
    try:
        browser.get("https://www.facebook.com/shares/view?id=1004270912921759")     #dummy fb share page to login
        browser.find_element_by_id('email').send_keys(email)
        browser.find_element_by_id('pass').send_keys(pwd)
        browser.find_element_by_id('loginbutton').click()
        print("Facebook login success!")
    except:
        browser.close()




def open_browser(type="firefox"):
    if type == "firefox":
        display = Display(visible=0, size=(1024, 768))
        display.start()
        
        browser = webdriver.Firefox()
    else:
        print("please use firefox browser...")
        print("stop running...")

    print("opening browser success")
    return (display, browser)





def close_browser(browser, display):
    browser.close()
    display.stop()






if __name__ == "__main__":

    browser = open_browser("firefox")
    fb_login(browser, email="lynnn.hong@gmail.com", pwd="hqam30018")
    
    url = "https://www.facebook.com/shares/view?id=1004270912921759"
    (share_list) = get_fb_share(browser, url)
    open('test.html','w').write(share_list)
    
    close_browser(browser, display)
    
    
    html = open("/home/ubuntu/py/facebook/150109_share/2015-01-07_1014702415211942.html", "r").read()
    p_id = int(1014702415211942)
    (usr_id, usr_name, usr_type, s_datetime, s_message) = parse_html(html, p_id)
    
