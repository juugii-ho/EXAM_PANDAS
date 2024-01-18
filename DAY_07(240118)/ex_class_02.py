# ------------------------------------------------------------------------------
# 자동차 클래스 : 현대자동차 직원이 프로그램을 만든다면...
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차 번호, 차 종류 (인스턴스 속성), 제조사(클래스 속성)
# 클래스 기능 : 주행한다, 정지한다, 후진한다
# ------------------------------------------------------------------------------
class Car:
    # 클래스 속성
    maker = '현대'

    # 생성자 메서드 => 객체 즉, 카 인스턴스 생성 메서드
    def __init__(self, wheel, color, number, kind):
        # 힙 영역에 저장
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind

    # 객체 즉, 카 인스턴스 멧더ㅡ
    def driving(self, where, who):
        print(f'{where}(으)로 "{who}"이/가 {self.number} 차를 타고 드라이빙하고 있다.')
    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지 했다.')
    def back(self):
        print(f'{self.number} 차가 후진 했다.')


# ---------------------------------------------------------
# 자동차 인스턴스 생성
# ---------------------------------------------------------

myCar = Car(19,'red', 6483, 'QM3')
secondCar = Car(20, 'hot pink', 7777, 'Genesis')

myCar.driving('집', '은우')
secondCar.back()


# ----------------------------------------------------------------------------------------
# 사랑 클래스
# 클래스 이름 : Love
# 클래스 속성 : kind, depth, happiness, decade
# 클래스 기능 : 새우, 깻잎, 금융치료, 데려다주기, 데이트, 같이아프기, 대신 죽어주기, 희생하기
# ----------------------------------------------------------------------------------------
class Love:
    feeling = '역동적'

    def __init__(self, kind):
        self.kind = kind
    def saewoo(self):
        print(f'{self}')

    def ggatIp(self):
        print()

    def money(self):
        print()

    def baredajugi(self):
        print()

# ----------------------------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : Calc
# 클래스 속성 : 브랜드, 종류, 색깔, 크기, 가격
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 => '속성' 또는 '기능에서 매개변수'로도 가능
# ----------------------------------------------------------------------------------------
class Calc:
    # 클래스변수
    maker = '카시오'
    _size=(7,15)

    # 객체 즉, 인스턴스 생성 메서드
    def __init__(self, kind, color, price, info):
        self.kind = kind
        self.color = color
        self.price = price
        self.data = 0
        # self.__size = (7,15)     # 비공개 속성     __속성명 : 클래스 밖에서 속성을 읽거나/쓰기 불가
        #                                                   어차피 인스턴스 안 생기므로 클래스 변수로 가면 됨
        self.__info = info         # 비공개 속성 : 인스터스 생성 시 계산기에 각인되는 정보

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드
    def getInfo(self):                         # 메서드로 작동
        return self.__info

    def setInfo(self, info):
        self.__info=info

    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) aptjem
    # => 속성 읽기/쓰기 방식으로 동작하도록 설정
    @property
    def info(self): return self.__info          # 속성으로 작동

    @info.setter
    def info(self, info): self.__info=info      # 속성으로 작동


    def plus(self, nums):
        self.data += nums
    def minus(self, nums):
        self.data -= nums
    def multi(self, nums):
        self.data *= nums
    def div(self, nums):
        if ~nums: return '0으로 나눌 수 없습니다.'
        self.data = self.data/nums
    def result(self):
        return self.data


# ----------------------------------------------------------------------------------------
# Calc 클래스로 인스턴스 생성 => 힙에 생성 : 인스턴스 변수 + 클래스 변수
#                                    인스턴스 메서드 사용 가능
# ----------------------------------------------------------------------------------------
c1 = Calc('공학용', '블랙', 10000, '초코')

# 인스턴스 속성 읽기 => 공개 속성만 읽기 가능
print(c1.data, c1.color, c1.kind)
# print(c1.__info) 는 안 보임

# 인스턴스 속성 변경 => 공개 속성만 읽기/쓰기 가능
c1.color = "빨강"

# 인스턴스 비공개 속성 읽기 ==> 전용의 메소드인 getter/setter 통해서 읽기/쓰기 가능
print(c1.getInfo(), c1.info) #c1.getInfo()를 통해 읽기 가능하게끔 메서드를 만들었지만 속성으로도 가능하게끔 만듦

# 인스턴스 비공개 속성 변경 ==> 위의 데코레이터가 공개형 속성 변경처럼 가능하게 만듦
c1.setInfo("내꺼")
c1.info = "내꺼"


# ----------------------------------------------------------------------------------------
# Calc 클래스로 계산기 정보 확인 => 클래스 변수만 확인 가능
#                             인스턴스 변수나 메서드 사용 불가능!!
#                             self 값이 없음!
# ----------------------------------------------------------------------------------------
# Calc.plus(10, 20)
# Calc.maker 생성하지 않은 상태에서 실행하면 메서드가 보이지만 생성된 객체가 없어서 self가 없으므로 실행하면 오류 발생

print(Calc.maker)
