__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is script for counting word frequency in the whole document.
"""



"""
A single input text must be a co-occurrence unit.
"""

def co_count(text, type, sep, var="", seed="undefined"):
    
    if var not in globals():
        globals()[var] = dict()
    exec("global %s" % var)
    token_dict = eval(var)
    
    if type == "text":
        tokens = set(text.split(sep))
    elif type == "token":
        tokens = set(token)
    elif type == "tokens":
        tokens = text
        
    if seed != "undefined":
        index = range(0, len(seed))
        for i in index:
            if seed[i] in tokens:
                for token in tokens:
                    if token == "":
                        continue
                    if token not in token_dict.keys():
                        token_dict[token] = 1
                    else:
                        token_dict[token] += 1    
        
    globals()[var] = token_dict

    
    
    
if __name__ == "__main__":
    #sample text
    s="""   가끔 실행중에 멈추는 0000 프로그램들이 있습니다. 
    이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다.
    ubuntu 시스템의 상황을 알려주는 시스템 모니터 333에 이 기능이 있습니다^^ ubuntu 14.04~"""
    s2 = "있습니다. 이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다."


    result = co_count(text=s, type="text", sep=" ", var = "foo", seed=["실행중에", "ubuntu"])
    print(result)


