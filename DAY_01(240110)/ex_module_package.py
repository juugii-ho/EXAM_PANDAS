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