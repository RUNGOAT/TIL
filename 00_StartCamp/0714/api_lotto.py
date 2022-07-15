import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'
response = requests.get(url).json()
lotto = []
drwNo = response.get('drwNo')
for x in range(1, 7):
    # key = f'drwtNo{x}'
    # print(response.get(key))

    a = response.get(f'drwtNo{x}')
    lotto.append(a)

    # lotto = response.get(f'drwtNo{x}') 는 X
    # int값을 넣을 수 없다
    

print(lotto)