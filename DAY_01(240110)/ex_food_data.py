file = 'food.txt'

kor_food, china_food =[],[]
foods={}

# 1번 방법 ========================================
# kind=''
#
# with open(file, mode='r', encoding='utf8') as f:
#     data = f.readline()
#     if not data.index("*"):
#         kind = '한식' if data[1:] == '한식' else '중식'
#     else:
#         if kind == '한식': kor_food.append(data)
#         else:
#             china_food.append(data)
#
# 2번 방법 ========================================
# key =''
# with open(file, mode='r', encoding='utf8') as f:
#     data = f.readline()
#     if not data.find('*'):
#         # kind = data[1:]
#         foods[data[1:]]=[]
#     else:
#         foods[key].append(data)
#
# 3번 방법 ========================================
with open(file, mode='r', encoding='utf8') as f:
    data = f.readlines()

# \n 없애려면 data[:-1]