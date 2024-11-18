#사전

cabinet = {3:"유재석", 100:"김태호"}          #사전은 {}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))                   #!!!get(?)일때 ?가 지정되지 않을 경우 None이 나오고 그대로 실행 하지만
                                        #   [?]일때 ?가 지정되지 않을 경우엔 그대로 실행 중지됨!!!
print(cabinet.get(5)) 
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)                     #있으면 True 없으면 False 캐비넷안에 3이라는 자료값이 있느냐 라는 뜻
print(5 in cabinet)

cabinet = {"A-3":"유재석 ", "B-100":"김태호"} # 정수말고 str도 가능

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)