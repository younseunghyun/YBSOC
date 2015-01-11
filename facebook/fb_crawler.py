__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.

#sudo pip install facebook-sdk
#don't install 'facebook'!!

This is originally under python27 but working on python34 also.
"""

import facebook 
import requests
import os
import json
import time

from easy_db import easy_mysql, insert_mysql

from fb_post import get_post
from fb_sub_object import get_sub_object
from fb_access_token import get_access_token


    


if __name__ == "__main__": 
    
    stop_datetime = "2014-01-01 00:00:00"
    os.environ['TZ'] = ':Asia/Seoul'; time.tzset()       #time zone setting
    
    # 0. getting access token of FB
    access_token = get_access_token(client_id = "325346580991946", 
                                    client_secret = "3bb9cb45ec5226411cf05b7f976e1d9d")     #app id, app secret
    graph = facebook.GraphAPI(access_token)
    target = "sbs8news"
    profile = graph.get_object(target)

    # 1. mysql server connection setting(amazon RDS)
    cfg_dict = dict(host='sbsnews.crsrypkw7bkm.ap-northeast-1.rds.amazonaws.com', usr='root', pwd='hqam30018', 
                    db='FACEBOOK')
    
    (con, cur) = easy_mysql(cfg_dict)
    cur.execute("SET NAMES latin1")         # couldn't changed RDS's character_set_server....
    
    
    # 2. getting the first FACEBOOK post data(the topmost pages on the wall)
    (n, c_dir, l_dir) = (0, 1, 1)
    posts = graph.get_connections(profile['id'], 'posts')
    
    while True:
        try:
            for post in posts['data']:
                if post['type'] == 'status':
                    continue
                n += 1
                p_dict = get_post(post, comments=True, likes=True)
                
                if str(p_dict['p_datetime']).startswith("2013") == True:
                    print(str(p_dict['p_datetime']))
                    print("fetched all posts until 2014-01-01")
                    exit()
                
                field_tuple = ('page_id', 'p_id', 'p_datetime', 'p_type', 'p_title', 'p_message', 'share_cnt', 'status_type', 'is_share', 'p_link', 'last_update')
                sql = "INSERT IGNORE INTO post(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) VALUES" % field_tuple
                sql += "(%d, %d, '%s', '%s', '%s', '%s', %d, '%s', %d, '%s', '%s');"
                var_tuple = tuple()
                for f in field_tuple:
                    var_tuple += (p_dict[f],)
                insert_mysql(cur, sql, var_tuple)
                con.commit()
                
                if n%150 == 0:
                    c_dir += 1
                if n%150 == 0:
                    l_dir += 1
                root_path = "/home/ubuntu/150108_result/"
                
                if p_dict['comments'] != "not exist" and str(p_dict['p_datetime'])[:19] > "2015-01-07 02:00:00":
                    path = root_path + "comments/" + str(c_dir)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filename = path + "/" + str(p_dict['p_id']) + ".json"
                    with open(filename, "w") as fp:
                        json.dump(p_dict['comments'], fp)
                
                if p_dict['likes'] != "not exist" and str(p_dict['p_datetime'])[:19] > "2015-01-07 02:00:00":
                    path = root_path + "likes/" + str(l_dir)
                    if not os.path.exists(path):
                        os.makedirs(path)
                    filename = path + "/" + str(p_dict['p_id']) + ".json"
                    with open(filename, "w") as fp:
                        json.dump(p_dict['likes'], fp)
                    
                print("finish post %i" % p_dict['p_id'])

            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            print(posts)
            break
    
    print("fetching all post finished")
    
    