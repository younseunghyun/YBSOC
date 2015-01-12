__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.
"""

import time
import os

from easy_db import easy_mysql, insert_mysql
from fb_share import open_browser, fb_login, get_fb_share, close_browser, parse_html




if __name__ == "__main__": 
    
    os.environ['TZ'] = ':Asia/Seoul'; time.tzset()       #time zone setting
    
    cfg_dict = dict(host='sbsnews.crsrypkw7bkm.ap-northeast-1.rds.amazonaws.com', usr='root', pwd='hqam30018', 
                    db='FACEBOOK')
    
    (con, cur) = easy_mysql(cfg_dict)
    cur.execute("SET NAMES latin1")         # couldn't change RDS's character_set_server....
    
    cur.execute("SELECT p_id, p_datetime FROM post ORDER BY p_datetime DESC;")
    rows = cur.fetchall()
    print("fetching all post ids finished...")
    print("the number of post: %i" % len(rows))
    
    (display, browser) = open_browser("firefox")
    fb_login(browser, email="lynnn.hong@gmail.com", pwd="hqam30018")        #login facebook
    print("open the first browser")
    
    n = 0
    for row in rows:            #each post
        n += 1
        if n % 100 == 0:
            close_browser(browser, display)     #refresh browser at every 100 rows
            (display, browser) = open_browser("firefox")
            fb_login(browser, email="lynnn.hong@gmail.com", pwd="hqam30018")        #login facebook
            print("\nopen browser %i\n" % (n/100)+2)
        
        (p_id, p_datetime) = (row[0], row[1])
        print("post %i started" % p_id)
        (share_html, last_update) = get_fb_share(browser, p_id)             #get facebook share list page(source html)
        
        if share_html == "no shares":
            continue
        
        share_list = parse_html(share_html, p_id)
        for share in share_list:
            var_tuple = share + (last_update,)
            if len(var_tuple) == 7:
                sql = "INSERT INTO post_share(p_id, s_usr_id, s_usr_name, s_usr_type, s_datetime, s_message, last_update) VALUES(%i, %i, '%s', '%s', '%s', '%s', '%s');"
            else:
                sql = "INSERT INTO post_share(p_id, s_usr_id, s_usr_name, s_usr_type, s_datetime, s_message, s_target_id, last_update) VALUES(%i, %i, '%s', '%s', '%s', '%s', %i, '%s');"
                sql_target = "INSERT INTO post_share_target(p_id, s_usr_id, s_target_id, s_target_name, s_target_type) VALUES(%i, %i, %i, '%s', '%s');"
                var_tuple_target = (var_tuple[0], var_tuple[1], var_tuple[6], var_tuple[7], var_tuple[8])
                var_tuple = var_tuple[0:7] + (var_tuple[9],)
                try:
                    insert_mysql(cur, sql_target, var_tuple_target)
                except TypeError:
                    print(var_tuple_target)
            try:
                insert_mysql(cur, sql, var_tuple)
            except TypeError:
                print(var_tuple)
            con.commit()
    close_browser(browser, display)
    
    