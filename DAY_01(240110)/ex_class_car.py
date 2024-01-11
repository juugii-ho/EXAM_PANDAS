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