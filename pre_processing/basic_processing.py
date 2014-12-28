__author__ = "lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is basic text pre-processing script for Korean.
"""

import re
import string




#rm tweet hashtag, url
#this is for tweet body text
def rm_entities(text):
    text = ' '.join(re.sub("(RT\s{1}@\S+)","",text).split())    #remove RT 
    text = ' '.join(re.sub("(@\S+)|(#\S+)|(http:\/\/\S+)|(https:\/\/\S+)\(pic.twitter.com\/S+\)","",text).split()) #remove mentions, hashtags and urls
    return text



def rm_specials(text, replace = " ", emoticon = False, exceptions = ""):
    exceptions = set(exceptions)        #split into set element
    removed = "".join([" " if x in string.punctuation and x not in exceptions else x for x in text])
    return removed
    
    

#When input type is token, the function returns empty string("") if the token is integer or float format.
def rm_numbers(text, type, replace = " "):     #type can be 'text' or 'token'
    if type == "text":
        regex_str = "( [0-9]+ | [0-9]+\.[0-9]+ )"
    elif type == "token":
        regex_str = "(^[0-9]+$|^[0-9]+\.[0-9]+$)"
        replace = ""
        
    removed = re.sub(regex_str, replace, text, count=0)
    return removed
    
    
def rm_whites(text):
    removed = " ".join(text.split())
    return removed




if __name__ == "__main__":
    #sample text
    s="""   가끔 실행중에 멈추는 0000 프로그램들이 있습니다. 
이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다.
ubuntu 시스템의 상황을 알려주는 시스템 모니터 333에 이 기능이 있습니다^^ ubuntu 14.04~"""


    #rm_whites(text)
    print("1. remove white-space")
    result1 = rm_whites(text = s)
    print(result1)
    
    
    #rm_specials(text[, replace(" "), emoticon(False), exceptions("")])
    print("2. remove special character")
    result2 = rm_specials(text = result1, replace = " ", emoticon = True, exceptions = ".,")
    rm_specials(result1)  #this is the simplest way
    print(result2)
    
    
    #rm_numbers(text, type[, replace(" ")])
    #'type' parameter can be 'text' or 'token'.
    print("3. remove numbers")
    result3 = rm_numbers(text = result2, type = "text", replace = "-")
    print(result3)
    
    for i in result2.split(" "):
        result3 = rm_numbers("token", i)
        if result3 != "":
            print(result3)
    
    #print("4. remove special character not emoticons")
    
    
    
    
    
    
    
    
    