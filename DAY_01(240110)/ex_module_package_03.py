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