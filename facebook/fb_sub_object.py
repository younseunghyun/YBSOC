__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"



from datetime import datetime
from dateutil import tz


from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Asia/Seoul')



def get_sub_object(item, item_type):
    result = dict()
    
    if item_type == "comment":
        result['c_id'] = int(item['id'].split("_")[1])
        time_tmp = item['created_time'].split("+")[0]
        time_formatted = datetime.strptime(time_tmp, '%Y-%m-%dT%H:%M:%S')
        time_formatted = time_formatted.replace(tzinfo=from_zone)
        result['c_datetime'] = time_formatted.astimezone(to_zone)
        
        result['c_usr_id'] = int(item['from']['id'])
        result['c_usr_name'] = item['from']['name'].replace("\'", "\\'")
        result['c_message'] = item['message'].replace("\'", "\\'").replace("\n", "\\n")
        result['c_like_cnt'] = item['like_count']
    elif item_type == "like":
        result['l_usr_id'] = int(item['id'])
        result['l_usr_name'] = item['name'].replace("\'", "\\'")

    return(result)

