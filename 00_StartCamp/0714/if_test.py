score = int(input())
# 사용자로부터 점수를 입력받아 학점 (A, B, C, D, F)를 출력하시오.

if score > 100 or score < 0:
    print('점수를 다시 입력하세요. 0점 이상 100점 이하')
else:
    if score >= 80:
        print('A')
    elif score >= 70:
        print('B')
    elif score >= 60:
        print('C')
    elif score >= 50:
        print('D')
    else:
        print('F')
