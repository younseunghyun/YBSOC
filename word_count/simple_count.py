__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is script for counting word frequency in the whole document.
"""


"""
IMPORTANT!

If the input text is the whole document, the parameter 'input_unit' is 'whole'.
If the input text is some part of the entire document such as a line, the parameter 'input_unit' is 'part'.
"""

"""
'type' parameter can be 'text', 'token' or 'tokens'(list, set or tuple)
If type is 'text', there must be the parameter 'sep' separating each tokens.

If token is empty string(""), it'll be removed.

Please don't use 'token_dict' as variable name of simple_count module's parameter.
"""

def simple_count(input_unit, text, type, sep, var="token_dict"):
    if input_unit == "part":
        if var not in globals():
            globals()[var] = dict()
        exec("global %s" % var)
        token_dict = eval(var)
    else:
        token_dict = dict()
    
    if type == "text":
        tokens = text.split(sep)
    elif type == "token":
        tokens = set(token)
    elif type == "tokens":
        tokens = text
        
    for token in tokens:
        if token == "":
            continue
        if token not in token_dict.keys():
            token_dict[token] = 1
        else:
            token_dict[token] += 1
    globals()[var] = token_dict
    return token_dict
        


    
    
if __name__ == "__main__":
    #sample text
    s="""   가끔 실행중에 멈추는 0000 프로그램들이 있습니다. 
    이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다.
    ubuntu 시스템의 상황을 알려주는 시스템 모니터 333에 이 기능이 있습니다^^ ubuntu 14.04~"""
    s2 = "있습니다. 이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다."


    #simple_count(input_unit, text, type[, sep])
    result = simple_count(input_unit = "whole", text = s, type = "text", sep = " ")
    print(result)
    
    for i in (s,s2):
        simple_count(input_unit = "part", text = i, type = "text", sep = " ", var = "foo")
    print(foo)      #foo is global variable


