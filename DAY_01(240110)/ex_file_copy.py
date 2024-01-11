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
