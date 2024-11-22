#슬라이싱

jumin = "030322-3635421"

print("성별 : " + jumin[7]) #[]는 0부터 시작
print("연 : " + jumin[0:2]) # 0부터 2직전까지(0, 1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
# print("생년월일 : " +jumin[0:6])
print("생년월일 : " +jumin[:6])     #9번줄과 같은 값임
# print("뒤 7자리 : " +jumin[7:14])
print("뒤 7자리 : " +jumin[7:])     #11번줄과 가은 값임
print("뒤 7자리 (뒤에부터) : " +jumin[-7:])
#맨 뒤에서 7번째부터 끝까지