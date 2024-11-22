#연산자

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 = 8 (제곱)
print(5%3) #  나머지 구하기 2
print(10%3) #1
print(5//3) #1 몫 구하기
print(10//3) #3 몫은 3
print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #3은 3과 똑같다 True
print(4 == 2) #4는 2와 같다 False
print(3+4 == 7)# True

print(1 != 3) #1은 3과 같지 않다.
print(not (1 == 3))
print(not(1 !=3))           # "=="는 같다라는 뜻이고 "!="는 같지 않다라는 뜻이다.

print((3 > 0) and (3 < 5)) # True
print((3 >0) & (3 <5)) #True        and와 &는 같은 뜻이고 그리고라는 뜻이기에 둘 조건 다 맞아야지만 True가 나온다

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True     or와 |는 같은 뜻이고, 또는이라는 뜻이기에 둘조건중 하나만 맞으면 True이다.

print(5 > 4 > 3) #True
print(5 > 4 > 7) #Flase
