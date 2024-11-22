#숫자 처리 함수

print(abs(-5)) # 5  abs라는 함수는 절댓값을 의미함
print(pow(4, 2)) # 4^2 = 4*4 = 16 pow는 승을 의미함 4의 2승 = 16
print(max(5, 12, 100)) # 100 max는 숫자들중 가장 큰값을 도출해냄
print(min(5, 12, 100)) # 5   min은 숫자들중 가장 작은값을 도출해냄
print(round(3.14)) # 3  round는 반올림을 의미함
print(round(4.56)) # 5

from math import *  # math라는 라이브러리를 이용하겠다는 뜻
print(floor(4.99)) #내림. 4
print(ceil(3.14)) #올림. 4
print(sqrt(16)) #제곱근. 4(루트)