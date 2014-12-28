import MeCab

m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ko-dic')

'''
Tag of mecab
	-https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=4

Result form of mecab parse expression
	-표현층 품사,의미부류, 받침유무,발음,type,시작형태소,끝형태소,원형표현,색인표현

Test sentence
	-파이썬은 물론이고 C#, Clojure, Julia등 31가지 언어에 대해 list comprehesion 방법을 설명하고 있다. 이 방법은 객체지향에 버금가는 혁신적인 프로그래밍 방법이라 할 수 있다. 인간의 사고와 비슷하게 프로그래밍하는 첫단추라고 해야할 것 같다.

Result

파이썬	NNP,*,T,파이썬,*,*,*,*,*

은	JX,*,T,은,*,*,*,*,*
물론	NNG,*,T,물론,*,*,*,*,*
이	VCP,*,F,이,*,*,*,*,*
고	EC,*,F,고,*,*,*,*,*
C	SL,*,*,*,*,*,*,*,*
#,	SY,*,*,*,*,*,*,*,*
Clojure	SL,*,*,*,*,*,*,*,*
,	SC,*,*,*,*,*,*,*,*
Julia	SL,*,*,*,*,*,*,*,*
등	NNB,*,T,등,*,*,*,*,*
31	SN,*,*,*,*,*,*,*,*
가지	NNBC,*,F,가지,*,*,*,*,*
언어	NNG,*,F,언어,*,*,*,*,*
에	JKB,*,F,에,*,*,*,*,*
대해	VV+EC,*,F,대해,Inflect,VV,EC,대하/VV+아/EC,*
list	SL,*,*,*,*,*,*,*,*
comprehesion	SL,*,*,*,*,*,*,*,*

and more...

'''
with open('mecab_test.txt','w') as fi:
	for line in m.parse('파이썬은 물론이고 C#, Clojure, Julia등 31가지 언어에 대해 list comprehesion 방법을 설명하고 있다. 이 방법은 객체지향에 버금가는 혁신적인 프로그래밍 방법이라 할 수 있다. 인간의 사고와 비슷하게 프로그래밍하는 첫단추라고 해야할 것 같다.'):
		fi.write(line)








