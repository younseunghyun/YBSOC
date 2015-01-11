__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"


import requests


    
def get_access_token(client_id, client_secret):
    oauth_args = dict(client_id = client_id,
                      client_secret = client_secret,
                      grant_type = "client_credentials")
    oauth_curl_url = "https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=%s"
    oauth_request = oauth_curl_url % (oauth_args['client_id'], oauth_args['client_secret'], oauth_args['grant_type'])
    response = requests.get(oauth_request)
    print("generating access token finished")
    return response.text.split("=")[1]