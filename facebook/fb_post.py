__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"



from datetime import datetime
from dateutil import tz


from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Seoul')




def get_post(post, comments, likes):
    '''for key in post.keys():
        print("%s : %s" % (key, post[key]))        #for test
    print("---   post end   ---")
    '''
    result = dict()
    
    result['page_id'] = int(post['id'].split("_")[0])
    result['p_id'] = int(post['id'].split("_")[1])
    
    time_tmp = post['created_time'].split("+")[0]
    time_formatted = datetime.strptime(time_tmp, '%Y-%m-%dT%H:%M:%S')
    time_formatted = time_formatted.replace(tzinfo=from_zone)
    result['p_datetime'] = time_formatted.astimezone(to_zone)
        
    try:
        message = post['message']
        if message.startswith("<") == True:
            try:
                split_indx = message.find(">")
                result['p_title'] = message[1:split_indx].replace("\'", "\\'")
                result['p_message'] = message[split_indx + 1:].strip().replace("\'", "\\'").replace("\n", "\\n")
            except:
                print(post)
        else:
            result['p_title'] = ""
            result['p_message'] = post['message'].replace("\'", "\\'").replace("\n", "\\n")
    except KeyError:
        result['p_message'] = ""
        result['p_title'] = ""
    
    try:
        result['p_link'] = post['link']
    except KeyError:
        result['p_link'] = ""
    
    try:
        result['share_cnt'] = post['shares']['count']
    except KeyError:
        result['share_cnt'] = -1
        
    result['p_type'] = post['type']
    
    try:
        result['status_type'] = post['status_type']
        if post['status_type'] == "shared_story":
            result['is_share'] = 1
        else:
            result['is_share'] = 0
    except KeyError:
        result['status_type'] = ""
        result['is_share'] = 0

    if comments == True:
        try:
            result['comments'] = post['comments']
        except KeyError:
            result['comments'] = "not exist"
    if likes == True:
        try:
            result['likes'] = post['likes']
        except KeyError:
            result['likes'] = "not exist"
    
    result['last_update'] = datetime.now()
    
    return(result)





def get_all_posts(graph, comments, likes, save):
    posts = graph.get_connections(profile['id'], 'posts')
    while True:
        try:
            [get_post(post, comments, likes, save) for post in posts['data']]
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
    
