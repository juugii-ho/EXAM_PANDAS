# ------------------------------------------------------------------------------------------------------
# 사용자 정의 클래스
# ------------------------------------------------------------------------------------------------------
# 클래스 정의 : 밤 하늘의 별을 저장하는 데이터
# 클래스 이름 : Star
# 클래스 속성 : 크기, 색상, 밝기 => 속성(attribute), 필드(field) => 변수
# 클래스 기능 : 반짝거린다, 떨어진다 => 함수(function), 메서드(method) => 함수
# ------------------------------------------------------------------------------------------------------
class Star:
    pass
# 이건 마치..
# def test():
#    pass
# ------------------------------------------------------------------------------------------------------
# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙 영역에 생성
# 생성 방법 => 클래스명(       )                          생성자     함수/메서드
#            클래스명(매개변수1)                          생성자     함수/메서드
#            클래스명(매개변수1, 매개변수2, ..., 매개변수N)     생성자     함수/메서드
#            - 속성의 갯수에 따라 매개변수가 증가
# ------------------------------------------------------------------------------------------------------
myStar = Star()      # 실행하면 class Star를 읽음. 저장을 하면 메모리영역을 차지
# name = "Hong"을 만들고 name.을 누를면 메서드가 보이듯이 class도 다양한 메서드 등이 보임
# myStar. 해보면 => 파이썬에서 모든 것은 object에서 시작됨. 그래서 class도 __init__등의 object를 상속받음

class Star:
    # 최상위 부모클래스 object로부터 상속받은 함수 즉, 메서드
    # 형태 def __XXX__()를 자동으로 상속받음
    # 나의 class에 맞도록 수정 즉, 리모델링해서 사용 => 오버라이드(override)
    def __init__(self, size, color, brightness):
        print(f'__init__() : {size}, {color}, {brightness}')
        # 힙 메모리 영역에 저장
        self.size=size                 # myStar의 size 5 주소를, self.size에 저장해주세요
        self.color=color               # myStar의 color dark yellow 주소를, self.color에 저장해주세요
        self.brightness=brightness     # myStar의 brightness 10 주소를, self.brightness에 저장해주세요

myStar= Star(5, 'dark yellow', 10)

# ------------------------------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 -> 객체변수명.속성명
# ------------------------------------------------------------------------------------------------------
print( myStar.color, myStar.brightness)
# ------------------------------------------------------------------------------------------------------
# 객체의 속성 정보 변경 -> 객체변수명.속성명 = 새로운 값
# ------------------------------------------------------------------------------------------------------
myStar.brightness = 7
print(myStar.color, myStar.brightness)

# ------------------------------------------------------------------------------------------------------

class Star:
    def __init__(self, size, color, brightness, name='알 수 없음'):       # name 추가
        print(f'__init__() : {size}, {color}, {brightness}, {name}')    # name 추가
        self.size=size
        self.color=color
        self.brightness=brightness
        self.name=name                                                  # name 추가

    # 별 클래스의 기능 => 메서드
    def drop(self):                                                     # 기능 추가
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원 빌어요~!')
        print(f'{self.color} 별이 하늘에서 떨어집니다. 소원 빌어요~!')

myStar= Star(5, 'dark yellow', 10)
yourStar = Star(10, 'red', 20, 'RedStar')


# ------------------------------------------------------------------------------------------------------
# 객체의 메서드 실행 -> 객체변수명.메서드명()
# ------------------------------------------------------------------------------------------------------
myStar.drop()
yourStar.drop()

print(f'클래스명.__dict__ : \n {Star.__dict__}')
print(f'인스턴스명.__dict__ : \n {myStar.__dict__}')
print(f'인스턴스명.__dict__ : \n {yourStar.__dict__}')

# 클래스명.__dict__ :
#  {'__module__': '__main__', '__init__': <function Star.__init__ at 0x104bf5310>, 'drop': <function Star.drop at 0x104bf53a0>, '__dict__': <attribute '__dict__' of 'Star' objects>, '__weakref__': <attribute '__weakref__' of 'Star' objects>, '__doc__': None}
# 인스턴스명.__dict__ :
#  {'size': 5, 'color': 'dark yellow', 'brightness': 10, 'name': '알 수 없음'}
# 인스턴스명.__dict__ :
#  {'size': 10, 'color': 'red', 'brightness': 20, 'name': 'RedStar'}

# ------------------------------------------------------------------------------------------------------

class Star:
    def __init__(self, size, color, brightness, name='알 수 없음', timezone='밤'):       # timezone 추가
        print(f'__init__() : {size}, {color}, {brightness}, {name}, {timezone}')      # timezone cnrk
        self.size=size
        self.color=color
        self.brightness=brightness
        self.name=name
        self.timezone=timezone

# 처럼 timezone을 쓸 수 있지만 모두에게 적용되는 밤이기 때문에 아래와 같이 '클래스 변수' 사용

class Star:
    # 클래스 변수/속성/필드 => 해당 클래스로 생선된 객체 즉, 인스턴스가 공유하는 속성
    timezone='밤'                     # 클래스 변수 timezone 추가

    def __init__(self, size, color, brightness, name='알 수 없음'):
        print(f'__init__() : {size}, {color}, {brightness}, {name}')
        self.size=size
        self.color=color
        self.brightness=brightness
        self.name=name

    # 별 클래스의 기능 => 메서드
    def drop(self):
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원 빌어요~!')
        print(f'{self.color} 별이 하늘에서 떨어집니다. 소원 빌어요~!')

myStar= Star(5, 'dark yellow', 10)
yourStar = Star(10, 'red', 20, 'RedStar')

# ------------------------------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 -> 객체변수명.속성명
# ------------------------------------------------------------------------------------------------------
print( myStar.color, myStar.brightness, myStar.timezone, Star.timezone)



# ------------------------------------------------------------------------------------------------------

class Star:
    timezone='밤'
    __privateValue=77               # 비공개 클래스 변수

    def __init__(self, size, color, brightness, name='알 수 없음'):
        print(f'__init__() : {size}, {color}, {brightness}, {name}')
        self.__size=size                # 비공개 인스턴스 속성
        self.color=color
        self.brightness=brightness
        self.name=name

    # 별 클래스의 기능 => 메서드
    def drop(self):
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원 빌어요~!')
        print(f'{self.color} 별이 하늘에서 떨어집니다. 소원 빌어요~!')

    # 비공개 인스턴스 속성에 접근하기 위한 메서드 => getter/setter 메서드
    # 비공개 인스턴스 속성을 읽어오는 메서드 get속성명() ===> 속성값
    # 비공개 인스턴스 속성에 값 설정 하는 메서드 set속성명(새로운값)
    def getSize(self):
        return self.__size
    def setSize(self, size):
        self.__size=size

    # 비공개 인스턴스 메서드 => 클래스 내부에서만 호출되는 메서드 ------------------------
    def __inner(self):
        print("나는 비공개 인스턴스 메서드")

myStar= Star(5, 'dark yellow', 10)
yourStar = Star(10, 'red', 20, 'RedStar')


# ------------------------------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 -> 객체변수명.속성명
# ------------------------------------------------------------------------------------------------------
# 인스턴스 속성에 직접 접근

print( myStar.color, myStar.brightness, myStar.timezone, Star.timezone)

# 인스턴스 속성에 간접 접근 => 메서드 제공 필수 getter/setter 메서드
print("현재 비공개 속성값 읽기 : ",  myStar.getSize())
# 현재 비공개 속성값 변경
myStar.setSize(100)
print(myStar.getSize())


# ------------------------------------------------------------------------------------------------------

class Star:
    timezone='밤'
    __privateValue=77

    def __init__(self, size, color, brightness, name='알 수 없음'):
        print(f'__init__() : {size}, {color}, {brightness}, {name}')
        self.__size=size
        self.color=color
        self.brightness=brightness
        self.name=name

    # 별 클래스의 기능 => 메서드
    def drop(self):
        print(f'{self.name} 별이 하늘에서 떨어집니다. 소원 빌어요~!')
        print(f'{self.color} 별이 하늘에서 떨어집니다. 소원 빌어요~!')
    def getSize(self):
        return self.__size
    def setSize(self, size):
        self.__size=size

    def __inner(self):
        print("나는 비공개 인스턴스 메서드")

    @staticmethod          # self 즉, 인스턴스를 생성하지 않는 함수
    def add():
        pass

class Love:
    @staticmethod
    def smile():
        pass

m = Love()
m.smile()
Love.smile() # 도 가능
#그러나 데코레이터 없이 Star.drop()    처럼 Star.drop(self)가 아니면 객체가 생성이 안 되기 때문에 실행이 안됨

    @classmethod
    def cc(cls):
        pass

cc.

myStar= Star(5, 'dark yellow', 10)
yourStar = Star(10, 'red', 20, 'RedStar')


# ------------------------------------------------------------------------------------------------------
# 객체의 속성 정보 읽기 -> 객체변수명.속성명
# ------------------------------------------------------------------------------------------------------
# 인스턴스 속성에 직접 접근

print( myStar.color, myStar.brightness, myStar.timezone, Star.timezone)

# 인스턴스 속성에 간접 접근 => 메서드 제공 필수 getter/setter 메서드
print("현재 비공개 속성값 읽기 : ",  myStar.getSize())
# 현재 비공개 속성값 변경
myStar.setSize(100)
print(myStar.getSize())


