#continue 와 break
absent = [2, 5] # 결석
no_book =[7]    #책이 없는놈임
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))
        