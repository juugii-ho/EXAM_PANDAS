# -------------------------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 읽기(Read)
# - 사용 내장 함수 : open()
# -------------------------------------------------------------------------------------------
# (1) open
file = open('message.txt')
print(f'file => {type(file)},{file}')
# file. read / write / close
# file = open('message.txt') 맥은 UTF-8 기본인 듯. 윈도우는 cp-949라서 encoding=utf8로 해야 보이는 듯


# (2) IO => read : 파일 안에 모든 내용 다 읽어오기
# fdata = file.read()
# print(f'data => {type(fdata)},{fdata}')

# (2) IO => read(n) : 지정된 숫자 만큼 문자를 파일에서 읽어오기
# fdata = file.read(5)  # 지정된 숫자 만큼 문자 읽기
#__n: int-1이 기본값인데 다 읽어라는 뜻이고, 5는 5바이트까지만
# print(f'data => {type(fdata)},{fdata}')
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
