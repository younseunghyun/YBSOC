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

from easy_db import easy_mysql, insert_mysql

from fb_post import get_post
from fb_sub_object import get_sub_object



if __name__ == "__main__": 

    sub_type = "likes"

    # 0. mysql server connection setting(amazon RDS)
    cfg_dict = dict(host='sbsnews.crsrypkw7bkm.ap-northeast-1.rds.amazonaws.com', usr='root', pwd='hqam30018', 
                    db='FACEBOOK')
    
    (con, cur) = easy_mysql(cfg_dict)
    cur.execute("SET NAMES latin1")         # couldn't changed RDS's character_set_server....
    
    root_path = "/home/ubuntu/150108_result/" + sub_type
    dir_list = os.listdir(root_path)
    for dir in dir_list:
        dir_path = root_path + "/" + dir
        file_list = os.listdir(dir_path)
        for file in file_list:
            with open(dir_path + "/" + file) as fp:
                likes = json.load(fp)
            n = 0
            while True:
                try:
                    for like in likes['data']:
                        n += 1
                        l_dict = get_sub_object(like, 'like')
                        field_tuple = ('p_id', 'l_usr_id', 'l_usr_name')
                        sql = "INSERT IGNORE INTO post_like(%s, %s, %s) VALUES" % field_tuple
                        sql += "(%d, %d, '%s');"
                        var_tuple = tuple()
                        var_tuple += (int(file.split(".")[0]),)      #p_id = file name
                        for f in field_tuple:
                            if f == 'p_id':
                                continue
                            var_tuple += (l_dict[f],)
                        insert_mysql(cur, sql, var_tuple)
                        con.commit()
                    likes = requests.get(likes['paging']['next']).json()
                except KeyError:
                    break
            print("finish file name %s" % file)
        print("finish directory %s" % dir)
    print("finish post likes %i" % n)
    
    