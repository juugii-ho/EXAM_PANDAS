# -------------------------------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드
# -------------------------------------------------------------------------------------------
filename = 'message.txt'
with open(filename, mode='r', encoding='utf8') as f:
    f.seek(5)                       # 해당 위치로 이동(1번 줄 5바이트)
    print(f.read(10))               # 부터 10바이트 읽어라
    print(f'현재 위치 : {f.tell}')    # 현재 위치가 어디인가
    f.seek(0)                       # 처음 위치로 이동(1번 줄 0바이트)
    print(f'현재 위치 : {f.tell}')    # 현재 위치가 어디인가
    print(f.name, f.closed)       # f.name 파일 이름 뭐니? f.closed() 파일 닫혔니? False

print(f.name, f.closed)           # f.name 파일 이름 뭐니? f.closed() 파일 닫혔니? True