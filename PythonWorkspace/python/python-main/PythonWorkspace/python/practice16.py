#튜플  -> 내용 변경이나 추가 불가능 하지만 리스트 보다 빠름
#리스트는 [] 이지만 튜플은 ()임
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스")  -> 추가 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)