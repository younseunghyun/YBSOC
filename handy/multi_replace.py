__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is multi replacing module using dictionary variable.
"""

import re




def multi_replace(input_dict, text):
    input_dict = dict((re.escape(k), v) for k, v in input_dict.items())
    pattern = re.compile("|".join(input_dict.keys()))
    replaced = pattern.sub(lambda m: input_dict[re.escape(m.group(0))], text)
    
    return replaced




if __name__ == "__main__":
    d = dict(before= "after", target= "replaced")
    text = "this is before, this is target"
    
    replaced = multi_replace(d, text)
    print(replaced)