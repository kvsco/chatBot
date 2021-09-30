from konlpy.tag import Okt

okt = Okt()

text = "아버지가 방에 들어갑니다."

morphs = okt.morphs(text)
print(f"형태소추출 : {morphs}")

pos = okt.pos(text)
print(f"형태소+품사추출:{pos}")

nouns = okt.nouns(text)
print(f"명사추출:{nouns}")

text2 = "오늘 날씨가 좋아욬ㅋㅋㅋ"
print(okt.normalize(text2))
print(okt.phrases(text2))