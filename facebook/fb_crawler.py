__author__ = "lynn"

"""
This is for crawling facebook text and meta information. A short example is provided in main function.

#sudo pip install facebook-sdk
#don't install 'facebook'!!

This is originally under python27 but working on python34 also.
"""

import facebook
import requests



def get_sub_object(object, type):
    sub_list = list()
    items = object['data']
    
    while True:
        try:
            for item in items:
                if type == "comment":
                    c_id = item['id']
                    c_created_time = item['created_time']
                    c_usr_id = item['from']['id']
                    c_usr_name = item['from']['name']
                    c_message = itme['message']
                    c_like_cnt = item['like_count']
                    sub_list.append(tuple(c_id, c_created_time, c_usr_id,c_usr_name, c_message, c_like_cnt))
                elif type == "like":
                    sub_list.append(tuple(item['id'], item['name']))
            items = requests.get(items['paging']['next']).json()
        except KeyError:
            break
    return(sub_list)





def get_post(post, fetching_comment, fetching_likes, save_location):
    '''for key in post.keys():
        print("%s : %s" % (key, post[key]))
    print("---   post end   ---")'''
    
    result = dict()
    
    result['object_id'] = post['object_id']
    try:
        result['created_time'] = post['updated_time']
    except KeyError:
        result['created_time'] = post['created_time']
    result['message'] = post['message']
    result['share_cnt'] = post['shares']['count']
    
    if fetching_comment == True:
        result['comments'] = get_sub_object(object = post['comments'], type = "comment")
    if fetching_likes == True:
        result['likes'] = get_sub_object(object = post['likes'], type = "like")
            
    return(result)
    #or doing something here such as storing using save_location



def get_all_posts(graph, fetching_comment, fetching_likes, save_location):
    posts = graph.get_connections(profile['id'], 'posts')
    while True:
        try:
            [get_post(post, fetching_comment, fetching_likes, save_location) for post in posts['data']]
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
    
    
    
def get_access_token(client_id, client_secret):
    oauth_args = dict(client_id = client_id,
                      client_secret = client_secret,
                      grant_type = "client_credentials")
    oauth_curl_url = "https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=%s"
    oauth_request = oauth_curl_url % (oauth_args['client_id'], oauth_args['client_secret'], oauth_args['grant_type'])
    response = requests.get(oauth_request)
    print("generating access token finished")
    return response.text.split("=")[1]
    


if __name__ == "__main__": 
    
    # 0. getting access token of FB
    access_token = get_access_token(client_id = "325346580991946", 
                                    client_secret = "3bb9cb45ec5226411cf05b7f976e1d9d")     #app id, app secret
    target = "sbs8news"
    graph = facebook.GraphAPI(access_token)
    
    
    # 1.fetching profile information of specific open account
    profile = graph.get_object(target)
    
    
    """ 2. fetching all posts in the wall
        default return value = {object_id, created_time, message, share_cnt} + [c_usr_id, c_usrname, comment, ] + [l_usr_id, l_usrname]
    """
    get_all_posts(graph = graph, fetching_comments = True, fetching_likes = True,
                  save = "some storing location")    # True = fetching not only posts but comments
    
    
    # 3. fetching pages the target likes
    
    # 4. fetching FB group profile, members
    
    # 5. fetching all people who like the target

    
    
    
    
    
    
    