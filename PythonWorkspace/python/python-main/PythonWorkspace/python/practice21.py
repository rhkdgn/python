#while 반복문 조건이 끝날때까지 계속함
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
    index -=1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

custom = "아이언맨"
inde = 1
while True:
    print("{0}님, 커피가 준비 되었습니다. 호출{1}회.".format(custom, inde))
    inde += 1
    