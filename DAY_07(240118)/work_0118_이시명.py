# 34

# 34.1

class person:
    def greeting(self):
        print('Hello')

james = person()

# 34.1.1

james.greeting()

# 34.1.2

a = int(10)
print(a)

b=list(range(10))
print(b)

c = dict(x=10, y=20)
print(c)

b = list(range(10))
b.append(20)
print(b)

a = 10
print(type(a))

b = [0,1,2]
print(type(b))

c = dict(x=10, y=20)
print(type(c))

maria = person()
print(type(maria))

# 34.1.3

class Person:
    pass

class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()

james=Person()
james.hello()

print(isinstance(james, Person))

def factorial(n):
    if not isinstance(n, int) or n <0:
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)


#34.2.

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

    def greeting(self):
        print(self.hello)

james =Person()
james.greeting()


#34.2.1

#34.2.2
class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name = '마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name' : '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

class Person:
    pass

maria = Person()
maria.name = '마리아'
print(maria.name)

james = Person()
# james.name

class Person:
    def greeting(self):
        self.hello = '안녕하세요.'

maria = Person()
# maria.hello

class Person:
    __slot__ = ['name', 'age']

maria = Person()
maria.name = '마리아'
maria.age = 20
# maria.address = '서울시 서초구 반포동'

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
maria = Person('마리아', 20, '서울시 서초구 반포동')
print(maria.name)

class Person:
    def __init__(self, name, age, address,wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
# print(maria.__wallet) -=10000

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

    def pay(self, amount):
        if amount > self.__wallet:
            print('돈이 모자라네..')
            return
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))


maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)
maria.pay(13000)

class Person:
    def __greeting(self):
        print('Hello')
    def hello(self):
        self.__greeting()

james = Person()
# james.__greeting()


class Annie:

    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print('티버 : 피해량 {0}'.format(self.ability_power*0.65+400))


health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()


# -------------------------------------------------------------------------------

# 35
# 35.1
# 35.1.1

class Person:
    bag = []

    def put_bag(self,stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Person:
    bag = []

    def put_bag(self,stuff):
        self.bag.append(stuff)


class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff)

print(Person.bag)

print(james.__dict__)
print(Person.__dict__)

#35.1.2

class Person:
    def __init__(self):
        self.bag= []

    def put_bag(self, stuff):
        self.bag.append(stuff)

james = Person()
james.put_bag('책')
maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

class Knight:
    __item_limit = 10

    def print_item_limit(self):
        print(Knight.__item_limit)

x = Knight()
x.print_item_limit()

# print(Knight.__item_limit)


class Person:
    '''사람 클래스입니다.'''

    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')

print(Person.__doc__)
print(Person.greeting.__doc__)

maria= Person()
print(maria.greeting.__doc__)

class Calc:
    @staticmethod
    def add(a,b):
        print(a + b)

    @staticmethod
    def mul(a,b):
        print(a * b)
Calc.add(10,20)
Calc.mul(10,20)

a = {1,2,3,4}
a.update({5})
print(a)
print(set.union({1,2,3,4},{5}))

#35.3

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))


james = Person()
maria = Person()

Person.print_count()

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour<=24 and minute <=59 and second <=60
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time




time_string = "23:35:59"


if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

# -------------------------------------------------------------------------------

#36

#36.1

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')

james = Student()
james.greeting()
james.study()

class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person))

#36.2.1

class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    def study(self):
        print('공부하기')

class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []
    def appeend_person(self, person):
        self.person_list.append(person)

#36.3

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
# print(james.hello)

#36. 3.1

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)

# 36.3.2
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    pass

james = Student()
print(james.hello)

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()
        self.school = '파이썬 코딩 도장'

# 36.4

class Person:
    def Student(self):
        print('안녕하세요.')

class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 파이썬 코딩 도장 학생이다.')

james = Student()
james.greeting()


class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        super().greeting()
        print('저는 파이썬 코딩 도장 학생입니다.')


james = Student()
james.greeting()


class Person:
    def greeting(self):
        print('안녕하세요.')


class University:
    def manage_credit(self):
        print('학점 관리')


class Undergraduate(Person, University):
    def study(self):
        print('공부하기')


james = Undergraduate()
james.greeting()
james.manage_credit()
james.study()


#36.5.1

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')


class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')


class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')


class D(B, C):
    pass


x = D()
x.greeting()

print(D.mro())

print(int.mro())
