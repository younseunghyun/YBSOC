__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is a simple script sending string data to server in kookmin university nlp lab(prof.강승식) 
to do Korean text auto-spacing.
"""

from io import BytesIO
import pycurl
from bs4 import BeautifulSoup
 
 

def auto_spacing(original, errors='strict'):
    url = 'http://nlp.kookmin.ac.kr/cgi-bin/asp.cgi'
    postfields = 'Question=%s&sendbutton=실행' % original
    
    storage = BytesIO()
    c = pycurl.Curl()
    
    try:
        c.setopt(c.URL, url)
        c.setopt(c.POSTFIELDS, postfields.encode('cp949', errors))
        c.setopt(c.WRITEFUNCTION, storage.write)
        c.perform()
        c.close()
        html = storage.getvalue().decode('cp949', errors)
        
        soup = BeautifulSoup(html)
        result = soup.find("table", {"class" : "tblindex01"}).findAll("td")[1].get_text(strip=True).split("출력: ")[1]
        return result
    
    except (UnicodeEncodeError, UnicodeDecodeError) as e:
        feedback = input("""* %s.\n
If you want to ignore(remove) that characters, press 'i'.
If you want to replace to another character, press 'r'.\n""" % e)
        if feedback.lower() == 'i':
            print("* OK. start ignoring some characters couldn't encoded or decoded to cp949...")
            return auto_spacing(original, 'ignore')
        elif feedback.lower() == 'r':
            print("* OK. start replacing some characters couldn't encoded or decoded to cp949 to character '?' or '\ufffd'...")
            return auto_spacing(original, 'replace')
        else:
            print("* Please re-check the button what you pressed.")
            return auto_spacing(original)
    except IndexError:
        print("""* While doing auto-spacing, the error has occurred. 
The input text is too long. Please split it into shorter ones. Stop processing...\n""")
        exit()
    
    
    
#example
if __name__ == "__main__":
    original = "안녕하세요저는홍수린입니다이건띄어쓰기데모입니다아무래도사전기반인것같네요사전에없는몇몇단어들은잘못나눠지는경우가있어요.불완전하긴한데쓸까요그냥?흐음"
    output = auto_spacing(original)
    print("input: %s" % original + "\n")
    print("output: %s" % output)