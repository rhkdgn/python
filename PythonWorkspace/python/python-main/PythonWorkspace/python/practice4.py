#변수

#애완동물을 소개해 주세요~(예제)
animal = "강아지"
name = "몽이"
age = 14
hobby = "산책"
is_adult = age >=13



print("우리집 " + animal + "의 이름은" + name + "입니다.")
#print(name + "는 str(age) + "살이며, " + hobby +"을 아주 좋아해요")     #age는 정수형, 즉 숫자이므로 문장속에 문자로 나타내기 위해 앞에 str이 붙음
print(name,"는 ", age,"살이며, ", hobby,"을 아주 좋아해요")              #+는 변수와 문장의 합침을 의미함 ,로 대체 할수 있지만 ,는 무조건 띄어쓰기가 들어감
                                                                       #또한, ,는 정수형을 문자형으로 바꾸기위한 str을 추가할 필요없음 
print(name + "는 어른일까요? " + str(is_adult))