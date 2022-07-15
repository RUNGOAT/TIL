import requests
url = 'https://api.agify.io/?name=jaegun'
response = requests.get(url).json()
name = response['name']
age = response.get('age')

print(f'{name}의 나이는 {age}살 입니다')