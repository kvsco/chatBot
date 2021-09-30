from konlpy.tag import Komoran

komo = Komoran(userdic='./user_dic.tsv')

text = "아버지가 방에 들어갑니다."

morphs = komo.morphs(text)
print(f"형태소추출 : {morphs}")

pos = komo.pos(text)
print(f"형태소+품사추출:{pos}")

nouns = komo.nouns(text)
print(f"명사추출:{nouns}")

text2 = "우리 챗봇은 엔엘피를 좋아해."
print(komo.pos(text2))