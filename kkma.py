from konlpy.tag import Kkma

kkma = Kkma()
text = "아버지가 방에 들어갑니다."

# 형태소만 추출 morpsh 토큰라이징
morphs = kkma.morphs(text)
print(morphs)

# 형태소,품사태그 추출 pos 
pos = kkma.pos(text)
print(pos)

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)

# 문장 분리
text2 = "오늘 날씨는 어때요? 내일은 덥다던데."
s = kkma.sentences(text2)
print(s) 