# -------------------------------------------------------------------------------------------
# 파일 입출력 => 출력 즉, 쓰기 (write)
# - 사용 내장 함수 : open(file, mode'rt', encoding='시스템 기본기')
# - encoding 설정 : 파일에 적용된 인코딩을 설정해야 함!!
# -------------------------------------------------------------------------------------------
filename = 'mydata.txt'
existfile = 'message.txt'

# (1) open => 쓰기(w) 모드의 경우 파일이 없으면 생성, 있으면 모든 내용 지움
file = open(filename, mode='w', encoding='utf-8')


# (2) write
# file.write("TEST")
file.write("12341234")      # 매 실행 시 마다 덮어쓰기하는 mode = 'w'
file.write("Ha Ha HA")      # 줄바꿈 문자가 없으면 이어서 써짐
file.write('''Ha Ha HA      
a
1111''')                    # '''는 줄바꿈 반영됨'''

file.writelines(['쓰고', '싶은', '것은', '리스트로', '쓰라는', '불편한', '기능'])
# 띄어쓰기 줄바꿈은 기호 넣어야 함
# list comprehension으로 해결할 수 있음

# 2단계 writelines() : 쓰고 싶은 거 있으면 리스트로 넣어라 물론 줄바꿈은 니 알아서 해라
file.writelines(i+"\n" for i in ["A", "B", "C"])

# (3)
file.close()