# 시리즈(Series) 살표보기
# - 판다스에서 데이터를 저장하는 자료 구조 중 하나 - 동일한 타입의 데이터를 연속된 메모리 공간에 저장 함 - 구성 : 인덱스 + 데이터 - 생성 : Series() 생성자 메서드
# (1)모듈 로딩 ----------------------------

import pandas as pd

# (2) 시리즈 객체 생성 ---------------------

sr = pd.Series([11,22,33])

print(sr)

print(type(sr))

# Series 객체의 속성(attributes)/필드(field) 살펴보기
# - 기본 : data, index,dtype
# - 읽기 : 객체변수명, 속성명
# - 쓰기 : 객체변수명, 속성명 = 새로운 값

# 현재 시리즈 객체에 저장된 인덱스 속성 확인
print(sr.index)

sr.values

print(array([11,22,33], dtype=int64))