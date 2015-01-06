__author__ = "Lynn"
__email__ = "lynnn.hong@gmail.com"

"""
This is script for POS-tagging Korean text using MeCab tagger module.
NNG    일반 명사
NNP    고유 명사
VV    동사
VA    형용사
MAG    일반 부사
SL    외국어
XR    어근
IC    감탄사

"""
import MeCab



def mecab_tagging(text):
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic')
    tag_filter = set(["NNG", "NNP", "VV", "VA", "MAG", "SL", "XR", "IC"])
    return_list = list()
    
    tagged_list = m.parse(text).split('\n')
    print(tagged_list)
    for tagged in tagged_list:
        if tagged == "EOS":
            break
        (word, meta) = tagged.split('\t')
        meta_list = meta.split(",")
        tag = meta_list[0]      #품사
        meaning_type = meta_list[1]     #의미부류
        if tag in tag_filter:
            print(word, tag, meaning_type)
            return_list.append((word, tag, meaning_type))
    return return_list



if __name__ == "__main__":
    #sample text
    s = """파이썬은 물론이고 C#, Clojure, Julia등 31가지 언어에 대해 list comprehesion 방법을 설명하고 있다. 
    이 방법은 객체지향에 버금가는 혁신적인 프로그래밍 방법이라 할 수 있다. 인간의 사고와 비슷하게 프로그래밍하는 첫단추라고 해야할 것 같다."""

    a = mecab_tagging(text = s)
    print(a)
    
"""
result is below

[('파이썬', 'NNP', '*'), ('물론', 'NNG', '*'), ('C', 'SL', '*'), ('Clojure', 'SL', '*'), ('Julia', 'SL', '*'), ('언어', 'NNG', '*'), ('list', 'SL', '*'), ('comprehesion', 'SL', '*'), ('방법', 'NNG', '*'), ('설명', 'NNG', '*'), ('방법', 'NNG', '*'), ('객체', 'NNG', '*'), ('지향', 'NNG', '*'), ('버금가', 'VV', '*'), ('혁신', 'NNG', '*'), ('프로그래밍', 'NNG', '*'), ('방법', 'NNG', '*'), ('있', 'VV', '*'), ('인간', 'NNG', '*'), ('사고', 'NNG', '*'), ('비슷', 'XR', '*'), ('프로그래밍', 'NNG', '*'), ('단추', 'NNG', '*'), ('같', 'VA', '*')]
"""
