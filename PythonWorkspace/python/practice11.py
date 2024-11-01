#문자열처리함수

python = "Python is Amazing"
print(python.lower()) # 다 소문자
print(python.upper()) # 다 대문자
print(python[0].isupper()) #0번째값이 대문자가 맞나요?
print(python[0].islower()) #0번째값이 소문자가 맞나여ㅛ?
print(len(python)) #python의 값이 몇자리인가요
print(python.replace("Python", "Java")) #문장속 바꿔줌

index = python.index("n")
print(index)            #문장속 n이  몇번째인지 알려줌
index = python.index("n", index + 1) # index의 값은 5번째임 그 다음에 나오는 n의 값수를 도출해내라는 명령어임
print(index)

print(python.find("Java"))  #찾는 값이 없을 경우 -1 도출
# print(python.index("Java")) #찾는 값이 없을 경우 오류가 남

print(python.count("n")) #n이 총 몇번 등장하느냐