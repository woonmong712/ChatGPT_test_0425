import random

print("가위, 바위, 보 중 하나를 선택하세요.")
user = input()

# 컴퓨터 가위바위보 선택
Rock_Paper_Scissors = ['가위','바위','보']
computer = random.choice(Rock_Paper_Scissors)

print(f"user : {user}")
print(f"computer : {computer}")
if user == computer:
    print("비김")
elif (user == '가위' and computer == '바위') or (user == '보' and computer == '가위') or (user == '바위' and computer == '보'):
    print("졌습니다.")
else:
    print("이겼습니다.")
