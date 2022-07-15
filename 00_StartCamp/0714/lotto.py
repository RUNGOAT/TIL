import random

numbers = random.choice(range(1, 46))
# print(numbers)
lucky = random.sample(numbers, 6)
print(lucky)
print(f'오늘의 행운의 번호는 {sorted(lucky)} 입니다.')
