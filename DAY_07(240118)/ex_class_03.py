# ------------------------------------------------------------------------------
# 2차원 점 클래스
# 클래스 이름 : Point2D
# 클래스 속성 : x, y, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보 출력
# ------------------------------------------------------------------------------
class Point2D:
    # 클래스 속성 => 없음

    # 객체 즉, 인스턴스 생성
    def __init__(self, x, y, color, shape, size):
        print('Point2D')
        self.x = x
        self.y = y
        self.color = color
        self.shape = shape
        self.size = size

    # 객체 즉, 인스턴스 메서드
    def draw(self):
        print(f"좌표 ({self.x}, {self.y})에 {self.shape} 그리기")

    def printInfo(self):
        print('2D')
        print(f"위치 : {self.x}, {self.y}")
        print(f"색상 : {self.color}")
        print(f"형태 : {self.shape}")

# ------------------------------------------------------------------------------
# 3차원 점 클래스
# 클래스 이름 : Point3D
# 클래스 속성 : x, y, z, color, shape, size
# 클래스 기능 : 그리기, 지우기, 정보 출력
# ------------------------------------------------------------------------------
import ex_class_02 as e2

class Point3D(Point2D,e2.Car):                    # Point2D,e2.Car 가 부모/슈퍼 클래스, Point3D 가 자식/서브 클래스
                                                  # 다중상속은 권장하지 않지만 가능은 함
    def __init__(self, x, y, z, color, shape, size):
        # 상속이면 부모 객체 생성 먼저하기 => super()
        super().__init__(x,y,color,shape,size)
        self.z = z
        print('Point3D')

    # 상속받은 부모의 메서드를 나의 취향에 맞게 수정 => 오버라이딩
    def printInfo(self):
        print('3D')
        print(f"위치 : {self.x}, {self.y}, {self.z}")
        print(f"색상 : {self.color}")
        print(f"형태 : {self.shape}")


p2 = Point2D(10, 10, 'red', 'circle', (10,10))
p3 = Point3D(5, 5, 5, 'yellow', 'rectangle', (3, 3, 3))

print(p3.x, p3.y, p3.z, p3.color, p3.shape, p3.size)

p3.printInfo()  # 자식 클래스에 있으면 자식 클래스의 메서드를 실행, 없으면 부모 클래스의 메서드를 실행


# 자율주행자동차 클래스 생성
# - 상속 적용하기

#
class JaCar(e2.Car):
    def __init__(self, wheel, color, number, kind, jayul):
        super().__init__(self, wheel, color, number, kind, jayul)
        self.jayul = jayul

    def driving(self, where, who):
        print(f'{where}(으)로 "{who}"이/가 {self.number} 차를 타고 드라이빙하고 있다.')
    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지 했다.')
    def back(self):
        print(f'{self.number} 차가 후진 했다.')

    def musk(self):
        print(f'{self.jayul} 주행 중입니다.')

class FlyCar(JaCar):

    def __init__(self, wheel, color, number, kind, jayul, flying):
        super().__init__(self, wheel, color, number, kind, jayul, flying)
        self.flying = flying

    def driving(self, where, who):
        print(f'{where}(으)로 "{who}"이/가 {self.number} 차를 타고 드라이빙하고 있다.')

    def stop(self, place):
        print(f'{self.number} 차가 {place}에 정지 했다.')

    def back(self):
        print(f'{self.number} 차가 후진 했다.')

    def musk(self):
        print(f'{self.jayul} 주행 중입니다.')

    def fly(self):
        print(f'{self.flying} 주행 중입니다.')