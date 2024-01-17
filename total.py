file_Object = open(file, mode='w', encoding=None)
# file 은 매개변수
# mode, encoding은 고정 매개변수

# -------------------------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(Read)
# - 사용 내장 함수 : open()
# -------------------------------------------------------------------------------------------
# (1) open
# file. read / write / close
# file = open('message.txt') 맥은 UTF-8 기본인 듯. 윈도우는 cp-949라서 encoding=utf8로 해야 보이는 듯


# (2) IO => read : 파일 안에 모든 내용 다 읽어오기
# fdata = file.read()
# print(f'data => {type(fdata)},{fdata}')

# (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기
# fdata = file.read(5)  # 지정된 숫자 만큼 문자 읽기
#__n: int-1이 기본값인데 다 읽어라는 뜻이고, 5는 5바이트까지만
# 윗 줄 (2) IO => read 파트 막으면 5바이트까지만 나옴

# fdata = file.read(5)
# print(f'data => {type(fdata)},{fdata}')
# Happy 끝난 위치에서부터 시작해 5바이트인' new ' 나옴

# (2) 10 => feadline() : '\n'기준으로 한 줄 읽어오기
# datas = []
# while True:
#     fline = file.readline()
#     if not fline: break
#     print(f'fline => {type(fline)},{fline}', end='')
#     # 원래 텍스트 파일에 줄바꿈\n + print의 매개변수 \n 있어서 두 줄로 넘어가는 것
#     # end=''해줘서 print의 매개변수를 바꾸면 한 줄 줄바꿈으로 바뀜
#     datas.append(fline)
# ㄴ 한 줄씩 받는 법 - 일부 생략하고 받을 때 필요함

datas = file.readlines()
# 위의 while문을 담아둔 readlines
print(datas)

# offset : 왼쪽에서부터 몇 칸 띄워졌는지
#012345678 ':'는 offset 8 위치

# (3) close
file.close()


# -------------------------------------------------------------------------------------------
# 입출력 코드 작성 시 권장하는 문법
# - open() / close() 함께 동작하는 경우의 IO에 권장
# - 예) 파일 입출력, 데이터베이스 등등
# - 문법 : with open()  as 별칭 :
# - close()를 알아서 처리해줌
# -------------------------------------------------------------------------------------------


# 쓰기
filename = 'fruits.txt'
with open(filename, mode='w', encoding='utf8') as f :
    f.write("사과\n")
    f.write("바나나\n")
    f.write("배\n")

# 읽기
with open(filename, mode='r', encoding='utf8') as f:
    print(f.read())


# -------------------------------------------------------------------------------------------
# 파일을 한하 선택 후 복사본 파일 생성 하기
# - 예시) message.txt ====> message_copy.txt
# -------------------------------------------------------------------------------------------

file = open('mydata.txt')
fdata = file.readlines()

with open('mydata_copy.txt', mode='w', encoding='utf8') as f :
    for list in fdata:
        f.write(list)

with open('mydata_copy2.txt', mode='w', encoding='utf8') as f2 :
    f2.writelines(i for i in fdata)
# 내가 한 것
# -------------------------------------------------------------------------------------------
filename= 'message.txt'

# 원본 파일에 내용 읽은 후 저장
with open(filename, mode='r', encoding='utf-8') as f:
    data = f.read()

# 복사본 파일에 내용 쓰기

with open('message.txt', mode='w', encoding='utf-8') as f:
    f.write(data)

# 원본 파일에 내용 읽은 후 to 새 파일에 바로 저장
with open(filename, mode='r', encoding='utf-8') as of:
    with open('message.txt', mode='w', encoding='utf-8') as nf:
        nf.write(of.read())

# -------------------------------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -------------------------------------------------------------------------------------------
filename = 'message.txt'
with open(filename, mode='r', encoding='utf8') as f:
    f.seek(5)                       # 해당 위치로 이동(1번 줄 5바이트)
    print(f.read(10))               # 부터 10바이트 읽어라
    print(f'현재 위치 : {f.tell}')    # 현재 위치가 어디인가
    f.seek(0)                       # 처음 위치로 이동(1번 줄 0바이트)
    print(f'현재 위치 : {f.tell}')    # 현재 위치가 어디인가
    print(f.name, f.closed)       # f.name 파일 이름 뭐니? f.closed() 파일 닫혔니? False

print(f.name, f.closed)           # f.name 파일 이름 뭐니? f.closed() 파일 닫혔니? True


'''
이미지는 mode=’rb’로 읽어야 함
seek을 사용할 때 글자 당 영어는 1바이트, 한글은 3바이트를 사용 함
import 모듈명 as 별칭 사용
'''

# --------------------------------------------------------------------------
# 모듈과 패키지
# - 관계
#   * 모  듈 : 특정 기능/목적의 변수, 함수, 클래스를 저장한 하나의 파이썬 파일 .py
#   * 패키지 : 특정 기능/목적의 모듈들을 담고 있는 단위
# - 문법: import 모듈명
#        import 패미지명, 모듈명
# --------------------------------------------------------------------------
# 사용할 모듈 로딩--------------------------------------------------------------
import math             # 내장 모듈, math
import math as m         # 모듈내에서 factorial 함수만 사용
from math import factorial              # 모듈 내에서 factorial 함수만 사용
from math import factorial as fac       # 모듈 내에서 factorial 함수명에 별칭

def factorial(x):
    print(f'{x}!')

# 모듈 내의 요소(변수, 함수, 클래스) 사용 방법
# => 모듈명, 변수
# => 모듈명, 함수()
print(math.pi, math.pow(2,3))
print(m.pi, m.pow(2,3))

# 모듈 내의 함수 1개를 직접 import한 경우

print(factorial(4))
print(fac(4))

# from math import *                    # 모듈명 붙여야 함
# import math                           # 모듈명 안 붙여도 됨

# --------------------------------------------------------------------------
# from math import *
# => 모듈 내의 모든 변수, 함수, 클래스 포함
# import math
#
# --------------------------------------------------------------------------
# 사용할 모듈 로딩--------------------------------------------------------------
from math import *

# 모듈명 없이 바로 사용 가능
print(pi, pow(2,3))

print(f'__name__ => {type(__name__)}, {__name__}')

# __XXX__ 변수          #  일반적으로 사용하지 않는 변수명, 함수명
# __XXX__() 함수        #  => 파이썬에 시스템에 필요한 경우 사용하는 변수를 __xx__로 네이밍 - 매직코드


# --------------------------------------------------------------------------
# from math import *
# => 모듈 내의 모든 변수, 함수, 클래스 포함
# 패키지 사용법
# --------------------------------------------------------------------------
# 사용할 모듈 로딩--------------------------------------------------------------
# import 패키지명.모듈명
import urllib.request as req                   # 이게 정석

# from 패키지명, import 모듈명
from urllib import error, parse
from http.client import HTTPResponse

dataObj = req.urlopen('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
# print(dataObj)      # <http.client.HTTPResponse object at 0x104631a60>
print(dataObj)

# 현재 상황에서는 패키지 설치는 conda install 패키지명 으로 설치

# # -------------------------------------------------
# # 자동차 관리 프로그램 만들기
# # - 엔진, 연료, 브랜드, 색상, 번호
# # - 전진, 후진, 좌회전, 우회전, 정지
# # -------------------------------------------------
#
# engine1 = '휘발유엔진'
# food1 = '휘발유'
# maker1 = '현대'
# color1 = '흰색'
# number1 = '111가1111'
#
# engine2 = '휘발유엔진'
# food2 = '휘발유'
# maker2 = '현대'
# color2 = '흰색'
# number2 = '111가2222'
#
# engine3 = '휘발유엔진'
# food3 = '휘발유'
# maker3 = '기아'
# color3 = '회색'
# number3 = '111가3333'
#
# def go(number): print(f'{number} 자동차가 전진')
# def back(number): print(f'{number} 자동차가 후진')
# def left_go(number): print(f'{number} 자동차가 좌회전')
# def right_go(number): print(f'{number} 자동차가 우회전')
# def stop(number): print(f'{number} 자동차가 정지')
#
# carDict = {'111가3333' : { 'engine': '휘발유엔진', 'color' : '흰색', 'maker' : '현대', 'autodriver':False},
#            '111가2222' : { 'engine': '경유엔진', 'color' : '회색', 'maker' : '기아', 'autodriver':False}
#            }
#
#
#
# # 자동차 관리 ----------------------------------------------------
# for k, v in carDict.items():
#     print(f'판매 차량 [{k}]')
#     for subK, subV in v.items():
#         print(f' - {subK} : {subV}')

# ----------------------------------------------------
# 자동차 관리 ----------------------------------------------------
# - 역할 : 자동차 관련 데이터, 기능을 모두 저장 관리하는 클래스
# - 문법
#   class 클래스명 :
#   <--> 코드
# ----------------------------------------------------
class Car:
    maker='현대'
    # 클래스 생성 시 필수로 사용되는 메서드
    # 힙 메모리에 속성들의 값을 저장해주는 역
    def __init__(self, engine_, food_, number_, color_):
        # 자동차 클래스가 가지는 속성을 메모리 힙에 저장
        print('__init__')
        self.engine=engine_
        # self.maker=maker_
        self.food=food_
        self.number=number_
        self.color=color_

    def go(self):
        print(f'{self.number} 자동차 전진')

    def back(self):
        print(f'{self.number} 자동차 후진')

    def stop(self):
        print(f'{self.number} 자동차 정지')

# 클래스로 자동차 객체 생성 --------------------------------
myCar = Car('휘발유엔진', '휘발유', '111가1111', '흰색')
myCar2 = Car('휘발유엔진', '휘발유',  '111가7777', '핫핑크색')


myCar.go()

# -------------------------------------------------
# 판다스 패키지 설치 확인 및 버전 체크
# -------------------------------------------------
import pandas as pd

# 버전 확인 -------------------------------------------------
print(pd.__version__)

# 데이터 파일 읽기 -------------------------------------------------
# 상대 경로 : 현재 파일을 기준으로 잡아서 경로를 설정
filename = '../DATA/used_cars.csv'

data = pd.read_csv(filename)
print(f'data => {type(data), data}')


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



