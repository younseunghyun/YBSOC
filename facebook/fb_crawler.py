"""
sudo pip install facebook-sdk
#don't install 'facebook'!!

this is under python27
"""


import facebook
import requests



def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['message'])




def get_all_posts(graph):
    posts = graph.get_connections(profile['id'], 'posts')
    while True:
        try:
            [some_action(post=post) for post in posts['data']]
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
    return response.text
    


if __name__ == "__main__": 
    access_token = get_access_token(client_id = "325346580991946", 
                                    client_secret = "3bb9cb45ec5226411cf05b7f976e1d9d")     #app id, app secret
    target = "sbs8news"
    
    graph = facebook.GraphAPI(access_token)
    profile = graph.get_object(target)
    print(profile)
    
    get_all_posts(graph)
    
    
    
    
    
    
    
    
    