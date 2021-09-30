from konlpy.tag import Komoran
import numpy as np

k = Komoran()

text = "오늘 날씨는 구름이 많네요."

nouns = k.nouns(text)
print(nouns)

dic = {}
for noun in nouns :
    if noun not in dic.keys():
        dic[noun] = len(dic)
        #걍 0부터 순서대로 value값 부여함
print(dic)

nb_classes = len(dic)
print(nb_classes)
target = list(dic.values())
print(target)
onehot_target = np.eye(nb_classes)[target]
print(onehot_target)