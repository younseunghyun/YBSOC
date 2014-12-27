__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is simple tutorial script letting you know how to use basic text pre-processing functions.
"""

from basic_processing import *
from auto_spacing import auto_spacing




#sample text written in Korean extracted from one of naver movie reviews
sample = open("./sample.txt", "r").read()

'''
sample="""   가끔 실행중에 멈추는 프로그램들이 있습니다. 
    이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다.
ubuntu 시스템의 top 5 상황을 알려주는 시스템 모니터 3에 이 기능이 있습니다^^"""
'''
#or you can use this shorter sentence for testing

input("This is the original samle text. Press any key.")
print(sample)
print("---------------------------------------------------\n")



#remove all successive white-space, new line(\n) and tab(\t)
#I think this is the clearest way to handle white-spaces. (personal recommendation)
input("1. remove all successive white-space, new line('\\n') and tab('\\t') example. Press any key.")
s1 = rm_whites(sample)
print(s1)
print("---------------------------------------------------\n")



#remove all white-space and pass auto-spacing function
#You can pass the second parameter as an error handle option for non-ascii characters('ignore' or 'replace' - default is 'strict')
input("2. auto-spacing example. This is spacing_error text. Press any key.")
spacing_error = sample.replace(" ", "").replace("\n", "")
print(spacing_error)

input("2. auto-spacing example. This is processed text. Press any key.")
s2 = auto_spacing(spacing_error)
print(s2)
print("---------------------------------------------------\n")



#remove numeric tokens from text(not alphanumeric)
input("3. remove numeric tokens from text(not alphanumeric) example. Press any key.")
s3 = rm_numbers(type="text", text=sample)
print(s3)
print("---------------------------------------------------\n")


#remove special characters from text
input("4. remove special characters from text example. Press any key.")
s4 = rm_specials(sample)
print(s4)

input("The default character to replace is 'space'. So I recommend you to use 'rm_whites' function after 'rm_specials' or 'rm_numbers'.\nThe result looks like this.")
print(rm_whites(s4))
print("---------------------------------------------------\n")
