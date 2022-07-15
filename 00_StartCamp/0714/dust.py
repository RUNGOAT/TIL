dust = 70

# dust 변수에 들어 있는 값을 기준으로 미세먼지 수치 정보 출력해보세요.

# if dust > 150:
#     print('매우나쁨')
# elif 150 >= dust > 80:  #파이썬만 가능!
#     print('나쁨')
# elif dust <= 80 and dust > 30:
#     print('보통')
# else:
#     print('좋음')

dust = 152

if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

