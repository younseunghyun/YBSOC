__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is script for handling exceptional terms which must not be removed from the original text. 
'random_generator' function is used to create mapping words randomly.
The simple usage guide is in the main function.
"""

import string
import random
import re
#from handy import multi_replace            #need multi_replace function from 'handy' directory





def exception_decode(path, text):
    file_path = path + "/exception_output.tsv"
    
    try:
        lines = open(file_path, 'r').readlines()
    except FileNotFoundError:
        print("There's no file named 'exception_output.tsv' in the path.\nPlease be sure that the exception list file name must be 'exception_output.tsv'.")
        print("Stop processing...\n")
        exit()
    decode_dict = dict()
    
    i = 0
    for line in lines:
        i += 1
        if i == 1:
            if len(line.replace('\n', '').split('\t')) == 3:
                print("The representative of each mapping line is not yet assigned.\nIf there're words having multiple synonyms, you'll be moved to interactive mode.")
        items = line.replace('\n', '').split('\t')
        if len(items) == 4:
            (id, words, random_word, rep) = items
            decode_dict[random_word] = words.split('\t')[int(rep) - 1]
        elif len(items) == 3:
            (id, words, random_word) = items
            if ";;;;;" in words:
                word_list = words.split(";;;;;")
                print("\nThese are synonyms of random key " + random_word + "\n" + ", ".join(word_list))
                rep_num = input("Please choose the number of representative word.(The leftmost one is '1') : ")
                words = word_list[int(rep_num) - 1]
            decode_dict[random_word] = words
    
    return multi_replace(decode_dict, text)





"""
The 'char' parameter can be 'upper', 'lower', 'digit' or combinations of these.
"""
def random_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase):
    chars = chars.replace("upper", string.ascii_uppercase)
    chars = chars.replace("lower", string.ascii_lowercase)
    chars = chars.replace("digit", string.digits)
    
    return ''.join(random.choice(chars) for x in range(size))





def exception_encode(path, random_size=10, random_rule=string.ascii_uppercase + string.ascii_lowercase):
    input_file_path = path + "/exception_input.tsv"
    output_file_path = path + "/exception_output.tsv"
    try:
        input_lines = open(input_file_path, 'r').readlines()
        output_file = open(output_file_path, 'w')
    except FileNotFoundError:
        print("There's no file named 'exception_input.tsv' in the input path.\nPlease be sure that the input file name must be 'exception_input.tsv'.")
        print("Stop processing...\n")
        exit()
    
    result_dict = dict()
    id_list = list()
    random_set = set()
    
    for line in input_lines:
        if line.startswith('#') or line == "" or line == " " or line == "\n":
            continue
        id = line.split('\t')[0]
        if id not in id_list:
            id_list.append(id)
        
    for id in id_list:
        while True:
            random_word = random_generator(random_size, random_rule)        #generating random word for mapping
            if random_word in random_set:    #for uniqueness
                pass
            else:
                break
        random_set.add(random_word)
        output_string = id + "\t%s\t" + random_word + "\n"
        words = ""
        for line in [x for x in input_lines if x.startswith(id)]:
            word = line.replace("\n", "").split('\t')[1]
            words += ";;;;;" + word
            result_dict[word] = random_word      #add element to result dictionary
        output_file.write(output_string % (words[5:]))   #write into random mapping text file
        print(output_string % (words[5:]))
        
    return result_dict
        
 
    



if __name__ == "__main__":
    
    #sample text
    s="""   가끔 실행중에 멈추는 0000 프로그램들이 있습니다. 
    이런 프로그램들을 강제 종료 시키는 쉬운 방법입니다.
    ubuntu 시스템의 상황을 알려주는 시스템 모니터 333에 이 기능이 있습니다^^ ubuntu 14.04~"""
    
    ex_dict = exception_encode(path = "./tutorial", random_size = 10, random_rule = 'upper'+'lower')
    encoded = multi_replace(ex_dict, s)
    decoded = exception_decode(path = "./tutorial", text = encoded)
    
    print("original text:\n" + s + "\n")
    print("encoded text:\n" + encoded + "\n")
    print("decoded text:\n" + decoded + "\n")
    

